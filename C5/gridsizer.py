import wx

class MyFrame(wx.Frame):
    def __init__(self,Parent,Title):
        super(MyFrame,self).__init__(Parent, title = Title,size = (600,500))
        self.panel = MyPanel(self)

class MyPanel(wx.Panel):
    def __init__(self,parent):
        super(MyPanel,self).__init__(parent)
        gridsizer = wx.GridSizer(4,4,5,5)
        for i in range(1,17):
            btn = "Btn" + str(i)
            gridsizer.Add(wx.Button(self,label = btn), 0, wx.EXPAND)  
        self.SetSizer(gridsizer)     

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(Parent = None, Title = "Grid Sizer")
        self.frame.Show()

        return True

        
app = MyApp()
app.MainLoop()