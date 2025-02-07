---
author: Mindusting
corrected: false
tags:
  - Programming/Java/GUI
title: GUI en Java
---

# CLASE JTABLE

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

%%
```java
package temp;

import java.awt.BorderLayout;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.table.JTableHeader;
import javax.swing.table.DefaultTableModel;
import javax.swing.JLabel;
import javax.swing.JRadioButton;

public class a extends JFrame {

    public a() {
        setTitle("JTable Example");

        DefaultTableModel table_model = new DefaultTableModel();
        String column_names [] = {"Patata", "Antonio", "Paco", "asdasd", null, null};
        table_model = new DefaultTableModel(column_names, 5);
        JTable jt = new JTable(table_model);
        
        JScrollPane sp = new JScrollPane(jt);
        add(sp);

        setSize(300, 200);
        setVisible(true);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    public static void main(String[] args) {
        new a(); 
    }
}
```
%%
