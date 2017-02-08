import requests,json


class Api:
    s = requests.session()
    user = ''
    pwd  = ''
    url  = 'https://passivetotal.org/api/account/login'

    def __init__(self, user, pwd):
        self.user = user
        self.pwd  = pwd

    def login(self):
        data        = '{"username":"%s","password":"%s"}' % (self.user, self.pwd)
        headers     = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json',
        'Referer': 'https://passivetotal.org/api/account/login',
        'Content-Length': '53',
        'Cookie': 'AWSALB=lh0jz9tegPLoaAg7QiCV/9UykI+RY8012sceBegJzPcr+EO1Ud/3bqxixRzsAqnfX6yM5BE5wFlmcLKbOlg+slBusWaNEFSLRapZPtOBmHPZnoEFAnkIS2JXwOPV; wooTracker=EB1yU2zbTC2C; _mkto_trk=id:455-NHF-420&token:_mch-passivetotal.org-1486447448265-32298; _ga=GA1.2.1267548199.1486447458; intercom-id-jh6w1mfi=a0055901-2ede-4dff-9d4a-075f40491b20; _gat_UA-42056430-2=1',
        'Connection': 'keep-alive'
    }
        response    = self.s.post(self.url, data=data, headers=headers);
        if response.status_code == 200:
            return True
        else:
            return False

    def start(self):
        if self.login():
            print('Login Success!!!')
            self.run()
        else:
            print('Login Failed!!!')

    def run(self):
        args    = input('>>>').split(' ')
        expList = {'exit':'exit'}
        try:
            if len(args) == 2:
                eval('self.'+args[0])(args[1])
            elif len(args) == 1:
                if args[0] in expList.keys():
                    eval(expList[args[0]])()
        except:
            print(args[0]+" not a function!")
        self.run()

    def subdomains(self, domain):
        url = 'https://www.passivetotal.org/api/dns/passive/subdomains?query=%s' % domain
        response = self.s.get(url)
        data = json.loads(response.text)
        domains = list(i['queryValue'] for i in data['results'])
        print(domains)

apiExp = Api('youemail@example.com','password');
apiExp.start();
