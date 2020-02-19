import wx

class MyFrame(wx.Frame):
    def __init__(self,Parent,Title):
        super(MyFrame,self).__init__(Parent, title = Title,size = (600,500))
        self.panel = MyPanel(self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(Parent = None, Title = "Our First window")
        self.frame.Show()

        return True

        
app = MyApp()
app.MainLoop()