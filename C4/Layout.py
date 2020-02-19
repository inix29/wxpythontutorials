import wx

class MyFrame(wx.Frame):
    def __init__(self,Parent,Title):
        super(MyFrame,self).__init__(Parent, title = Title,size = (600,500))
        self.panel = MyPanel(self)

class MyPanel(wx.Panel):
    def __init__(self,parent):
        super(MyPanel,self).__init__(parent)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.label1 = wx.StaticText(self, label = "This is a label1", style =wx.ALIGN_CENTER)
        vbox.Add(self.label1, 0, wx.EXPAND)
        self.label2 = wx.StaticText(self, label = "This is a label2", style =wx.ALIGN_CENTER)
        vbox.Add(self.label2, 0, wx.EXPAND)
        self.label3 = wx.StaticText(self, label = "This is a label3", style =wx.ALIGN_CENTER)
        hbox.Add(self.label3, 0, wx.EXPAND)
        self.label4 = wx.StaticText(self, label = "This is a label4", style =wx.ALIGN_CENTER)
        hbox.Add(self.label4, 0, wx.EXPAND)
        vbox.Add(hbox)
        self.SetSizer(vbox)
         

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(Parent = None, Title = "Box Sizer")
        self.frame.Show()

        return True

        
app = MyApp()
app.MainLoop()