                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                import webbrowser
print("this is the 3nd version of web searcher has the ability to search web without hyperlinks")
print('whatsapp(w)\npractically(p)\nto enter url(link)\nbing tab(b)\nGoogle(g)\nsearch normally(tex)')
print('whatsapp + practically(ess)\nto open all (all)')
inp = input('enter the input')
if inp == 'link':
    link = input('enter the url to open in your default browser')
    webbrowser.open('https://' + link)
elif inp == 'tex':
    link2 = input('enter the text you need to search to open in your default browser')
    webbrowser.open(link2)
elif inp == 'b':
    webbrowser.open('https://www.bing.com/')
elif inp == 'w':
    webbrowser.open('https://web.whatsapp.com/')
elif inp == 'p':    
    webbrowser.open('