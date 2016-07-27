#!/usr/bin/python

import xml.sax
import json
import operator

class CamposHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.dict = {}
      self.total = 0. 

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      #if tag == "Campos":
         #print "*****Campos*****"

   # Call when an elements ends
   def endElement(self, tag):
      tag_n_perc = self.dict.get(tag,None);
      if tag_n_perc is None :
	 self.total = self.total + 1.
         self.dict.update({self.CurrentData:1./self.total});
      else :
	 tag_n_perc = tag_n_perc + 1./self.total
         self.dict.update({self.CurrentData:tag_n_perc});
	 
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = CamposHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("campos.xml")

   sorted_dict = sorted(Handler.dict.items(), key=operator.itemgetter(1),reverse=True)

   #json_out = json.dumps(Handler.dict);
   json_out = json.dumps(sorted_dict[0:20]);

   print json_out
   
