#!/usr/bin/env python
from tika import parser


parsed = parser.from_file('Project_web.pptx')
print(parsed["metadata"]) #To get the meta data of the file
print(parsed["content"]) # To get the content of the file