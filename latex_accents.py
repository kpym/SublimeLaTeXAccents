# coding=utf-8
import sublime, sublime_plugin
import re

class LatexAccentsCommand(sublime_plugin.TextCommand):
	def run(self, edit, action="decode"):
		# --- save position to restore at the end
		vpos = self.view.viewport_position()

		# --- get regions to decode/encode
		regions = []
		empty_positions = []
		restoreEmpty = False

		for region in self.view.sel() :
			if region.empty():
				empty_positions.append(self.view.rowcol(region.a))
			else :
				regions.append(region)
		if not regions :
			# if all regions are empty
			# get the entire document
			regions = [sublime.Region(0, self.view.size())]
			# and indicate to restore empty positions at the end
			restoreEmpty = True

		# --- chose encode/decode/remove dictionary
		if action == "decode" :
			dict = latex_read_dict
		elif action == "encode" :
			dict = latex_write_dict
		elif action == "remove" :
			dict = remove_dict
		else :
			print 'Error in latex-accents : action \''+action+'\' unknown !'
			return

		edit = self.view.begin_edit()
		# ---------------------------
		# replace accents in all regions (in reverse order)
		# ---------------------------
		for region in reversed(regions) :
			text = self.view.substr(region)
			for key in dict:
				text = text.replace(key,dict[key])
			# and make the replacement
			self.view.replace(edit, region, text)
		# ---------------------------
		self.view.end_edit(edit)

		# --- restore empty positions if necessary
		if restoreEmpty :
			self.view.sel().clear()
			for point in empty_positions :
				self.view.sel().add(self.view.text_point(point[0],point[1]))

		# --- move the viewport to the original position
		self.view.set_viewport_position((0,0),False)
		self.view.set_viewport_position(vpos,False)

	def description(action="decode") :
		# I don't know where this description is visible
		if action == "decode" :
			return("Decode LaTeX accents like \'e to letters with accents like é.")
		elif action == "encode" :
			return("Encode letters with accents like é to LaTeX accents like \'e.")
		elif action == "remove" :
			return("Remove accents frome letters, for example 'é' became 'e'.")
		else :
			return("undefined action")

	def is_visible(self) :
		# visible only in LaTeX files
		return re.search("LaTeX", self.view.settings().get('syntax'))

# ---------------------------------------- READ DICTIONARY
latex_read_dict = {
"{!`}" : u"¡",
"{\\pounds}" : u"£",
"{\\S}" : u"§",
"{\\copyright}" : u"©",
"{\\pm}" : u"±",
"{\\P}" : u"¶",
"{\\cdot}" : u"·",
"{?`}" : u"¿",
"{\\div}" : u"÷",
"{\\times}" : u"×",
"{\\o}" : u"ø",
"{\\O}" : u"Ø",
"{\\`A}" : u"À",
"{\\'A}" : u"Á",
"{\\^A}" : u"Â",
"{\\~A}" : u"Ã",
"{\\\"A}" : u"Ä",
"{\\AA}" : u"Å",
"{\\AE}" : u"Æ",
"{\\c{C}}" : u"Ç",
"{\\`E}" : u"È",
"{\\'E}" : u"É",
"{\\^E}" : u"Ê",
"{\\\"E}" : u"Ë",
"{\\`I}" : u"Ì",
"{\\'I}" : u"Í",
"{\\^I}" : u"Î",
"{\\\"I}" : u"Ï",
"{\\~N}" : u"Ñ",
"{\\`O}" : u"Ò",
"{\\'O}" : u"Ó",
"{\\^O}" : u"Ô",
"{\\~O}" : u"Õ",
"{\\\"O}" : u"Ö",
"{\\OE}" : u"Œ",
"{\\`U}" : u"Ù",
"{\\'U}" : u"Ú",
"{\\^U}" : u"Û",
"{\\\"U}" : u"Ü",
"{\\'Y}" : u"Ý",
"{\\ss}" : u"ß",
"{\\`a}" : u"à",
"{\\'a}" : u"á",
"{\\^a}" : u"â",
"{\\~a}" : u"ã",
"{\\\"a}" : u"ä",
"{\\aa}" : u"å",
"{\\ae}" : u"æ",
"{\\c{c}}" : u"ç",
"{\\`e}" : u"è",
"{\\'e}" : u"é",
"{\\^e}" : u"ê",
"{\\\"e}" : u"ë",
"{\\`\\i}" : u"ì",
"{\\'\\i}" : u"í",
"{\\^\\i}" : u"î",
"{\\\"\\i}" : u"ï",
"{\\~n}" : u"ñ",
"{\\`o}" : u"ò",
"{\\'o}" : u"ó",
"{\\^o}" : u"ô",
"{\\~o}" : u"õ",
"{\\\"o}" : u"ö",
"{\\oe}" : u"œ",
"{\\`u}" : u"ù",
"{\\'u}" : u"ú",
"{\\^u}" : u"û",
"{\\\"u}" : u"ü",
"{\\'y}" : u"ý",
"{\\\"y}" : u"ÿ",
"\\`{A}" : u"À",
"\\'{A}" : u"Á",
"\\^{A}" : u"Â",
"\\~{A}" : u"Ã",
"\\\"{A}" : u"Ä",
"\\AE{}" : u"Æ",
"\\`{E}" : u"È",
"\\'{E}" : u"É",
"\\^{E}" : u"Ê",
"\\\"{E}" : u"Ë",
"\\c{C}" : u"Ç",
"\\`{I}" : u"Ì",
"\\'{I}" : u"Í",
"\\^{I}" : u"Î",
"\\\"{I}" : u"Ï",
"\\~{N}" : u"Ñ",
"\\`{O}" : u"Ò",
"\\'{O}" : u"Ó",
"\\^{O}" : u"Ô",
"\\~{O}" : u"Õ",
"\\\"{O}" : u"Ö",
"\\OE{}" : u"Œ",
"\\`{U}" : u"Ù",
"\\'{U}" : u"Ú",
"\\^{U}" : u"Û",
"\\\"{U}" : u"Ü",
"\\'{Y}" : u"Ý",
"\\`{a}" : u"à",
"\\'{a}" : u"á",
"\\^{a}" : u"â",
"\\~{a}" : u"ã",
"\\\"{a}" : u"ä",
"\\ae{}" : u"æ",
"\\c{c}" : u"ç",
"\\`{e}" : u"è",
"\\'{e}" : u"é",
"\\^{e}" : u"ê",
"\\\"{e}" : u"ë",
"\\`{\\i}" : u"ì",
"\\'{\\i}" : u"í",
"\\^{\\i}" : u"î",
"\\\"{\\i}" : u"ï",
"\\~{n}" : u"ñ",
"\\`{o}" : u"ò",
"\\'{o}" : u"ó",
"\\^{o}" : u"ô",
"\\~{o}" : u"õ",
"\\\"{o}" : u"ö",
"\\oe{}" : u"œ",
"\\`{u}" : u"ù",
"\\'{u}" : u"ú",
"\\^{u}" : u"û",
"\\\"{u}" : u"ü",
"\\'{y}" : u"ý",
"\\\"{y}" : u"ÿ",
"\\`A" : u"À",
"\\'A" : u"Á",
"\\^A" : u"Â",
"\\~A" : u"Ã",
"\\\"A" : u"Ä",
"\\`E" : u"È",
"\\'E" : u"É",
"\\^E" : u"Ê",
"\\\"E" : u"Ë",
"\\`I" : u"Ì",
"\\'I" : u"Í",
"\\^I" : u"Î",
"\\\"I" : u"Ï",
"\\~N" : u"Ñ",
"\\`O" : u"Ò",
"\\'O" : u"Ó",
"\\^O" : u"Ô",
"\\~O" : u"Õ",
"\\\"O" : u"Ö",
"\\`U" : u"Ù",
"\\'U" : u"Ú",
"\\^U" : u"Û",
"\\\"U" : u"Ü",
"\\'Y" : u"Ý",
"\\`a" : u"à",
"\\'a" : u"á",
"\\^a" : u"â",
"\\~a" : u"ã",
"\\\"a" : u"ä",
"\\`e" : u"è",
"\\'e" : u"é",
"\\^e" : u"ê",
"\\\"e" : u"ë",
"\\`\\i" : u"ì",
"\\'\\i" : u"í",
"\\^\\i" : u"î",
"\\\"\\i" : u"ï",
"\\~n" : u"ñ",
"\\`o" : u"ò",
"\\'o" : u"ó",
"\\^o" : u"ô",
"\\~o" : u"õ",
"\\\"o" : u"ö",
"\\`u" : u"ù",
"\\'u" : u"ú",
"\\^u" : u"û",
"\\\"u" : u"ü",
"\\'y" : u"ý",
"\\\"y" : u"ÿ"
}


# ---------------------------------------- WRITE DICTIONARY
latex_write_dict = {
u"¡" : "{!`}",
u"£" : "{\\pounds}",
u"§" : "{\\S}",
u"©" : "{\\copyright}",
u"±" : "{\\pm}",
u"¶" : "{\\P}",
u"·" : "{\\cdot}",
u"¿" : "{?`}",
u"÷" : "{\\div}",
u"×" : "{\\times}",
u"ø" : "{\\o}",
u"Ø" : "{\\O}",
u"À" : "\\`A",
u"Á" : "\\'A",
u"Â" : "\\^A",
u"Ã" : "\\~A",
u"Ä" : "\\\"A",
u"Å" : "{\\AA}",
u"Æ" : "{\\AE}",
u"Ç" : "\\c{C}",
u"È" : "\\`E",
u"É" : "\\'E",
u"Ê" : "\\^E",
u"Ë" : "\\\"E",
u"Ì" : "\\`I",
u"Í" : "\\'I",
u"Î" : "\\^I",
u"Ï" : "\\\"I",
u"Ñ" : "\\~N",
u"Ò" : "\\`O",
u"Ó" : "\\'O",
u"Ô" : "\\^O",
u"Õ" : "\\~O",
u"Ö" : "\\\"O",
u"Œ" : "{\\OE}",
u"Ù" : "\\`U",
u"Ú" : "\\'U",
u"Û" : "\\^U",
u"Ü" : "\\\"U",
u"Ý" : "\\'Y",
u"ß" : "{\\ss}",
u"à" : "\\`a",
u"á" : "\\'a",
u"â" : "\\^a",
u"ã" : "\\~a",
u"ä" : "\\\"a",
u"å" : "{\\aa}",
u"æ" : "{\\ae}",
u"ç" : "\\c{c}",
u"è" : "\\`e",
u"é" : "\\'e",
u"ê" : "\\^e",
u"ë" : "\\\"e",
u"ì" : "{\\`\\i}",
u"í" : "{\\'\\i}",
u"î" : "{\\^\\i}",
u"ï" : "{\\\"\\i}",
u"ñ" : "\\~n",
u"ò" : "\\`o",
u"ó" : "\\'o",
u"ô" : "\\^o",
u"õ" : "\\~o",
u"ö" : "\\\"o",
u"œ" : "{\\oe}",
u"ù" : "\\`u",
u"ú" : "\\'u",
u"û" : "\\^u",
u"ü" : "\\\"u",
u"ý" : "\\'y",
u"ÿ" : "\\\"y",
}

# ---------------------------------------- REMOVE DICTIONARY
remove_dict = {
u"À" : "A",
u"Á" : "A",
u"Â" : "A",
u"Ã" : "A",
u"Ä" : "A",
u"Å" : "A",
u"Æ" : "AE",
u"Ç" : "C",
u"È" : "E",
u"É" : "E",
u"Ê" : "E",
u"Ë" : "E",
u"Ì" : "I",
u"Í" : "I",
u"Î" : "I",
u"Ï" : "I",
u"Ñ" : "N",
u"Ò" : "O",
u"Ó" : "O",
u"Ô" : "O",
u"Õ" : "O",
u"Ö" : "O",
u"Œ" : "OE",
u"Ù" : "U",
u"Ú" : "U",
u"Û" : "U",
u"Ü" : "U",
u"Ý" : "Y",
u"ß" : "ss",
u"à" : "a",
u"á" : "a",
u"â" : "a",
u"ã" : "a",
u"ä" : "a",
u"å" : "a",
u"æ" : "ae",
u"ç" : "c",
u"è" : "e",
u"é" : "e",
u"ê" : "e",
u"ë" : "e",
u"ì" : "i",
u"í" : "i",
u"î" : "i",
u"ï" : "i",
u"ñ" : "n",
u"ò" : "o",
u"ó" : "o",
u"ô" : "o",
u"õ" : "o",
u"ö" : "o",
u"œ" : "oe",
u"ù" : "u",
u"ú" : "u",
u"û" : "u",
u"ü" : "u",
u"ý" : "y",
u"ÿ" : "y",
}
