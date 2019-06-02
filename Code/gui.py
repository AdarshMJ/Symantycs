from __future__ import unicode_literals
import spacy
import os
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')
from nltk import sent_tokenize
import tqdm
import time
import wx
import wx.lib.filebrowsebutton

m1=[]
m2=[]
m3=[]
nlp = spacy.load('en_core_web_lg')
def get_file_contents(filename):
        with open(filename, 'r') as filehandle:  
            filecontent = (filehandle.read().decode('utf8'))
            return (filecontent) 

window=wx.App()

class s_report(wx.Frame):
    def __init__(self):
       
        wx.Frame.__init__(self,None,-1,"Lexei - an intelligent evaluation engine",size=(700,500))
        self.panel=wx.Panel(self,-1)
#        self.SetIcon(wx.Icon('/Users/adarsh/Desktop/logo_16x16.ico', wx.BITMAP_TYPE_ICO))
        menu=wx.MenuBar()
        file_menu=wx.Menu()        
        file_menu.Append(301,"Quit")
        self.Bind(wx.EVT_MENU,self.Quit,id=301)    
        help_menu=wx.Menu()
        help_menu.Append(302,"About")
        self.Bind(wx.EVT_MENU,self.about,id=302)        
        menu.Append(file_menu,"File")
        menu.Append(help_menu,"Help")
        
        wx.MessageBox('The answer script was automatically loaded from the directory...', 'Info', wx.OK | wx.ICON_INFORMATION)
        wx.StaticText(self.panel,-1,"Lexei is an intelligence enabled software for evaluating and grading paper-based answer scripts",pos=(10,10)) 
        wx.StaticText(self.panel,-1,"This is a beta program evaluating physics answer scripts.",pos=(10,30))
        wx.StaticText(self.panel,-1,"How much marks should be assigned if all the answers are correct?",pos=(10,100))
        wx.StaticText(self.panel,-1,"How much marks should be assigned if the answers are partially right? (Say about 60%)",pos=(10,125))
        wx.StaticText(self.panel,-1,"How much marks should be assigned if answers are wrong?",pos=(10,150))
       
        self.one=wx.TextCtrl(self.panel,-1,pos=(430,100),size=(60,20))
        self.two=wx.TextCtrl(self.panel,-1,pos=(560,125),size=(60,20))
        self.three=wx.TextCtrl(self.panel,-1,pos=(400,150),size=(60,20))
        wx.Button(self.panel,201,"Done",pos=(10,200))
        self.Bind(wx.EVT_BUTTON,self.Done,id=201)
        self.SetMenuBar(menu)  
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Centre()
        self.Show()
##        
    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()
 
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        wx.StaticText(self.panel,-1,"Powered By : ",pos=(80,235))
        bmp = wx.Bitmap("/Users/adarsh/Desktop/bgg.png")
        dc.DrawBitmap(bmp, 40, 250)
            
    def Done(self,event):

        m1=[]
        m2=[]
        m3=[]
        r1=[]
        r2=[]
        r3=[]
        
        m1.append(int(self.one.GetValue()))
        m2.append(int(self.two.GetValue()))
        m3.append(int(self.three.GetValue()))
        wx.MessageBox('The answer script was automatically loaded from the directory...', 'Info', wx.OK | wx.ICON_INFORMATION)
        file1 = "/Users/adarsh/Desktop/grading/Script1.txt"
        file2 = "/Users/adarsh/Desktop/grading/Keyans.txt"
        read1 = get_file_contents(file1)
        read2 = get_file_contents(file2)
        token1 =  sent_tokenize(read1)
        iter2 = sent_tokenize(read2)
        token2 = iter2[1::2]     
        i=1
        numofquestions = len(token2)
        wx.StaticText(self.panel,-1,"Number of Questions in the Question Paper:",pos=(10,350))
        wx.StaticText(self.panel,-1,str(numofquestions),pos=(10,370))
        
      

        wx.MessageBox('Evaluation and Grading the Answer Script...', 'Info', wx.OK | wx.ICON_INFORMATION)
        for i in  tqdm.tqdm(range(len(zip(token1,token2)))):
            z = nlp(unicode((token1)[i])).similarity(nlp(unicode((token2)[i])))
            time.sleep(0.1)
            print token1[i]  
            print token2[i]      
            print z
            if (z>0.90):
                r1.append(m1[0])
            elif(0.60<z<0.85):
                r2.append(m2[0])    
            elif(z<0.59):
                r3.append(m3[0])           
            i = i+1    
        Marks1 = sum(r1)
        Marks2 = sum(r2)
        Marks3 = sum(r3)
        Total = (Marks1+Marks2+Marks3)
        mcarried = numofquestions*m1[0]
                 
       
        
        wx.StaticText(self.panel,-1,"Total Marks for the examination : ",pos=(10,425))
        wx.StaticText(self.panel,-1,str(mcarried),pos=(360,425))  
        
        wx.StaticText(self.panel,-1,"Marks awarded for Questions found right:",pos=(10,445))
        wx.StaticText(self.panel,-1,str(Marks1),pos=(360,445))
        
        wx.StaticText(self.panel,-1,"Marks awarded for Questions with 60% right answer:",pos=(10,465))
        wx.StaticText(self.panel,-1,str(Marks2),pos =(360,465))
        
        wx.StaticText(self.panel,-1,"Marks awarded for Questions which are wrong :",pos=(10,485))
        wx.StaticText(self.panel,-1,str(Marks3),pos=(360,485))
        
         
        
        
        wx.StaticText(self.panel,-1,"Total Marks obtained by the individual:",pos=(10,515))
        wx.StaticText(self.panel,-1,str(Total),pos=(360,515))
        
      
       
        
    def Quit(self,event):
        self.Close()
    def about(self,event):
        self.about=wx.AboutDialogInfo()
        self.about.SetName("Lexei - Beta - v.1.0")
        self.about.SetCopyright("(c) 2018 Symantycs")
        self.about.SetWebSite("https://symantycs.github.io")
        self.about.AddDeveloper("Adarsh - https://adarshmj.github.io")
        wx.AboutBox(self.about)
s_report()
window.MainLoop()