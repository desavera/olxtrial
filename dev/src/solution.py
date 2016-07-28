#!/usr/bin/python

import xml.sax
import json
import operator

class SolutionHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""

      self.dict_campos = {}
      self.total = 0. 
      self.bairro = ""
      self.dict_bairros = {}

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      #if tag == "Campos":
         #print "*****Campos*****"

   # Call when an elements ends
   def endElement(self, tag):
      tag_n_perc = self.dict_campos.get(tag,None);
      if tag_n_perc is None :
	 self.total = self.total + 1.
         self.dict_campos.update({self.CurrentData:1./self.total});
      else :
	 tag_n_perc = tag_n_perc + 1./self.total
         self.dict_campos.update({self.CurrentData:tag_n_perc});

      if self.CurrentData == "Bairro":
         bairro_count = self.dict_bairros.get(self.bairro,0);
         bairro_count = bairro_count + 1
         self.dict_bairros.update({self.bairro:bairro_count});
         #print "Nome:", self.bairro, " Ocorreu :" , bairro_count
         self.CurrentData = ""

   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "Bairro":
         self.bairro = content
	 
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = SolutionHandler()
   parser.setContentHandler(Handler)
   
   parser.parse("http://ofertas.brbrokers.com.br/OLX/dff/sao_caetano_sul.xml")

   sorted_dict_campos = sorted(Handler.dict_campos.items(), key=operator.itemgetter(1),reverse=True)

   solution = json.dumps({'campos':sorted_dict_campos[0:20],'top_10_bairros':Handler.dict_bairros});

   print solution
