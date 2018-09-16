import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400, 400))

        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        self.CreateStatusBar()

        filemenu = wx.Menu()
        aboutItem = filemenu.Append(wx.ID_ABOUT, "&About", "Info")
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        filemenu.AppendSeparator()
        exitItem = filemenu.Append(wx.ID_EXIT, 'E&xit', "Terminate")
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")

        self.SetMenuBar(menuBar)
        self.Show(True)

    def OnAbout(self, e):
        '''Handle About Click in File Menu'''
        dlg = wx.MessageDialog(self, "My App bitch", 'About', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, e):
        '''Handle Exit Click in File Menu'''
        self.Close(True)



app = wx.App(False)

frame = MainWindow(None, 'Hello')

# frame.Show(True)

app.MainLoop()
