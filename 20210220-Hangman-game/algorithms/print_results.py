#Import functions
import algorithms.hangman as results
        
def make_html():
    "getting results to html page"
    
    with open("Results_web.html","w") as results_page:
        results_page.write("<html>\n <head>\n <title>HANGMAN</title>\n</head>\n<body>\n")
        results_page.write("<h1 align='center'>!!YOUR HANGMAN ROUND RESULTS!!</h1>")
        results_page.write("<h2 align='center'>PLAYER NAME: "+results.user_name +" </h2>")
        for i in range(results.game_count):
            results_page.write("<h3 align='center'> Game No. "+str(i+1)+"</h3>")
            results_page.write("<table border="'2'", width="'300'" align='center'>")
            results_page.write("<tr><td>Word given</td>\n<td>"+results.word_given[i]+"</td></tr>")
            results_page.write("<tr><td>Tries given</td>\n<td>"+str(results.turns_given[i])+"</td></tr>")
            results_page.write("<tr><td>Tries used</td>\n<td>"+str(results.turns_used[i])+"</td></tr>")
            results_page.write("<tr><td>Game outcome</td>\n<td>"+results.game_outcome[i]+"</td></tr></table><br>")

        results_page.write("<h3 align='center'> Final results</h3>")   
        results_page.write("<table border="'2'", width="'300'" align='center'>")
        results_page.write("<tr><td>Games won</td>\n<td>"+str(results.win_count)+"</td></tr>")
        results_page.write("<tr><td>Games lost</td>\n<td>"+str(results.loss_count)+"</td></tr>")
        results_page.write("<tr><td>Total games played</td>\n<td>"+str(results.game_count)+"</td></tr></table></html>")

    



