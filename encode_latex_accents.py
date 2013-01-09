# coding=utf-8
import sublime, sublime_plugin
import re

class EncodeLatexAccentsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# take all the document text and put it in 'ducument' string
		region = sublime.Region(0, self.view.size())
		document = self.view.substr(region)
		# replace all
		for key in latex_write_dict:
			document = document.replace(key,latex_write_dict[key])
		# and make the replacement
		edit = self.view.begin_edit()
		self.view.replace(edit, region, document) 
		self.view.end_edit(edit)

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
u"Ä" : "\\""A",
u"Å" : "{\\AA}",
u"Æ" : "{\\AE}",
u"Ç" : "\\c{C}",
u"È" : "\\`E",
u"É" : "\\'E",
u"Ê" : "\\^E",
u"Ë" : "\\""E",
u"Ì" : "\\`I",
u"Í" : "\\'I",
u"Î" : "\\^I",
u"Ï" : "\\""I",
u"Ñ" : "\\~N",
u"Ò" : "\\`O",
u"Ó" : "\\'O",
u"Ô" : "\\^O",
u"Õ" : "\\~O",
u"Ö" : "\\""O",
u"Ù" : "\\`U",
u"Ú" : "\\'U",
u"Û" : "\\^U",
u"Ü" : "\\""U",
u"Ý" : "\\'Y",
u"ß" : "{\\ss}",
u"à" : "\\`a",
u"á" : "\\'a",
u"â" : "\\^a",
u"ã" : "\\~a",
u"ä" : "\\""a",
u"å" : "{\\aa}",
u"æ" : "{\\ae}",
u"ç" : "\\c{c}",
u"è" : "\\`e",
u"é" : "\\'e",
u"ê" : "\\^e",
u"ë" : "\\""e",
u"ì" : "{\\`\\i}",
u"í" : "{\\'\\i}",
u"î" : "{\\^\\i}",
u"ï" : "{\\""\\i}",
u"ñ" : "\\~n",
u"ò" : "\\`o",
u"ó" : "\\'o",
u"ô" : "\\^o",
u"õ" : "\\~o",
u"ö" : "\\""o",
u"ù" : "\\`u",
u"ú" : "\\'u",
u"û" : "\\^u",
u"ü" : "\\""u",
u"ý" : "\\'y",
u"ÿ" : "\\""y",
}