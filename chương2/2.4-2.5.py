import xml.dom.minidom
def main():

  doc = xml.dom.minidom.parse("sample.xml");

  print(doc.nodeName)
  print(doc.firstChild.tagName)

  expertise = doc.getElementsByTagName("expertise")
  print("%d expertise:" % expertise.length)
  for skill in expertise:
    print(skill.getAttribute("name"))
if __name__=="__main__":
  main();