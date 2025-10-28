---
author: Mindusting
corrected: false
tags:
  - Programming/Java
title: XML en Java
---

# XML EN JAVA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

```java
public class User {
    private int    id   = 0;
    private int    age  = 0;
    private String name = null;
    

    public User(String name, int age) {
        this.id   = 0;
        this.name = name;
        this.age  = age;
    }
    
    public User(int id, String name, int age) {
        this.id   = id;
        this.name = name;
        this.age  = age;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

```java
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

public class UserManager {

    private String filePath   = null;
    private String entityName = null;


    public UserManager() {
        this.filePath   = "users.xml";
        this.entityName = "user";
    }


    public void saveDocument(File file, Document doc)
    throws TransformerException {
        TransformerFactory tf = TransformerFactory.newInstance();
        Transformer        t  = tf.newTransformer();
        t.transform(new DOMSource(doc), new StreamResult(file));
    }

    public Document loadDocument(File file)
    throws ParserConfigurationException, IOException, SAXException {
        DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
        DocumentBuilder        db  = dbf.newDocumentBuilder();
        return db.parse(file);
    }

    public void createNewDocument(File file, String rootName)
    throws ParserConfigurationException, IOException, SAXException,
    TransformerException {
        DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
        DocumentBuilder        db  = dbf.newDocumentBuilder();
        Document doc = db.newDocument();
        Element root = doc.createElement(rootName);
        doc.appendChild(root);
        this.saveDocument(file, doc);
    }

    public List<User> select_all()
    throws ParserConfigurationException, IOException, SAXException {
        List<User> users = new ArrayList<User>();

        Document doc     = null;
        NodeList nodes   = null;
        Element  element = null;

        doc   = this.loadDocument(new File(this.filePath));
        nodes = doc.getElementsByTagName(this.entityName);

        for (int i = 0; i < nodes.getLength(); i++) {
            element = (Element) nodes.item(i);

            int    id   = Integer.parseInt(element.getAttribute("id"));
            int    age  = Integer.parseInt(element.getAttribute("age"));
            String name = element.getAttribute("name");

            users.add(new User(id, name, age));
        }

        return users;
    }
    
    public void insert(User user)
    throws ParserConfigurationException, IOException, SAXException,
    TransformerException {
        Document doc        = null;
        Element  root       = null;
        Element  newElement = null;

        doc        = this.loadDocument(new File(this.filePath));
        root       = doc.getDocumentElement();
        newElement = doc.createElement(this.entityName);

        newElement.setAttribute("id",   String.valueOf(user.getId()));
        newElement.setAttribute("name", user.getName());
        newElement.setAttribute("age",  String.valueOf(user.getAge()));

        root.appendChild(newElement);

        this.saveDocument(new File(this.filePath), doc);
    }
    
    public void update(User user)
    throws ParserConfigurationException, IOException, SAXException,
    TransformerException {
        Document doc     = null;
        NodeList nodes   = null;
        Element  element = null;

        doc   = this.loadDocument(new File(this.filePath));
        nodes = doc.getElementsByTagName(this.entityName);

        for (int i = 0; i < nodes.getLength(); i++) {
            element = (Element) nodes.item(i);

            int elementId = Integer.parseInt(element.getAttribute("id"));
            if (elementId != user.getId()) {
                continue;
            }

            element.setAttribute("age",  String.valueOf(user.getAge()));
            element.setAttribute("name", user.getName());
            break;
        }

        this.saveDocument(new File(this.filePath), doc);
    }
    
    public void delete(User user)
    throws ParserConfigurationException, IOException, SAXException,
    TransformerException {
        Document doc     = null;
        NodeList nodes   = null;
        Element  element = null;

        doc   = this.loadDocument(new File(this.filePath));
        nodes = doc.getElementsByTagName(this.entityName);

        for (int i = 0; i < nodes.getLength(); i++) {
            element = (Element) nodes.item(i);

            int elementId = Integer.parseInt(element.getAttribute("id"));
            if (elementId != user.getId()) {
                continue;
            }

            element.getParentNode().removeChild(element);
            break;
        }

        this.saveDocument(new File(this.filePath), doc);
    }
}

```
