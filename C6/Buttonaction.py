import wx


class MyFrame(wx.Frame):
    def __init__(self, Parent, Title):
        super(MyFrame, self).__init__(Parent, title=Title, size=(600, 500))
        self.panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.label = wx.StaticText(self, label="hello world!")
        sizer.Add(self.label, 1, wx.EXPAND)
        self.btn = wx.Button(self, label="click me")
        sizer.Add(self.btn, 0)
        self.btn.Bind(wx.EVT_BUTTON, self.onClickMe)
        self.SetSizer(sizer)

    def onClickMe(self, event):
        self.label.SetLabelText("Text Has Been Changed")


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(Parent=None, Title="Button Events")
        self.frame.Show()

        return True


app = MyApp()
app.MainLoop()
