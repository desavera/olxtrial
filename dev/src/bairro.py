#!/usr/bin/python

import xml.sax
import json

class BairroHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.bairro = ""
      self.dict = {}

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      #if tag == "Bairro":
         #print "*****Bairro*****"

   # Call when an elements ends
   def endElement(self, tag):
      if self.CurrentData == "Bairro":
         bairro_count = self.dict.get(self.bairro,0);
         bairro_count = bairro_count + 1
         self.dict.update({self.bairro:bairro_count});
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
   Handler = BairroHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("bairro.xml")

   json_out = json.dumps(Handler.dict);

   print json_out
   
