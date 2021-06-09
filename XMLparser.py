import xml.etree.ElementTree as ET

def strip_tag_name(elem):
    tag = elem.tag
    idx = tag.rfind("}")
    if idx != -1:
        tag = tag[idx + 1:]
    return tag

def parser(fname):
    exclude = ["register", "record"]
    data = {}
    for event, elem in ET.iterparse(fname, events=("start","end")):
        tag_name = strip_tag_name(elem)
        if event == "start" and tag_name not in exclude:
            data[tag_name] = elem.text
        if event == "end" and tag_name == "record":
            yield(data)
            data = {}
        elem.clear()

if __name__ == "__main__":
    for record in parser("dataset/data.xml"):
        print(record)
