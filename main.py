import tkinter
import cloudscraper

def GetCookies():
    kue.delete('1.0','1.9999')
    useragent.delete('1.0','1.9999')
    cookie_value, user_agent = cloudscraper.get_cookie_string(ment.get())
    kue.insert(tkinter.INSERT,format(cookie_value))
    useragent.insert(tkinter.INSERT,format(user_agent))
    return

main_window = tkinter.Tk()
main_window.geometry('450x450+400+200')
main_window.title('Cloudflare Cookies Scraper')
ment = tkinter.StringVar()

labelurl = tkinter.Label(main_window,text='Url. Ex: https://mangadex.org').pack()
urlentry = tkinter.Entry(main_window,text=ment,width='50').pack()
labelkue = tkinter.Label(main_window, text = 'Cookies').pack()
kue = tkinter.Text(main_window,height='5')
kue.pack()
labeluseragent = tkinter.Label(main_window,text='User-Agent').pack()
useragent = tkinter.Text(main_window,height='5')
useragent.pack()
getcookies = tkinter.Button(main_window,text='Get Cookies & User Agent',command=GetCookies).pack()

main_window.mainloop()
