import xml.dom.minidom as minidom

def main():
    doc = minidom.parse("C:/Users/SUDIPTA/OneDrive/Documents/60148_prod_prem_20220512_ra.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    batch=doc.getElementsByTagName("Batch")
    batchId=batch[0].getAttribute("id")
    print("Batch Id : "+batchId)

    packages=doc.getElementsByTagName("Package")

    for package in packages:
        packageId=package.getAttribute("id")
        print("Package id : " +packageId)
        trackingNumber=package.getElementsByTagName("Tracking Number")
        print("Tracking Number : "+trackingNumber[0].firstChild.nodeValue)
        cards=package.getElementsByTagName("Card")
        print(cards.length)
        for card in cards :
            ginNumber=card.getAttribute("GINNumber")
            accessCardNumber=(card.getElementsByTagName("MSN"))[0].firstChild.nodeValue
            print(" Employee Number : "+ginNumber+" and access card number : "+accessCardNumber)



main()