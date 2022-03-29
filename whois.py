# author: ononemli

from pyfiglet import Figlet
from time import sleep
import whois

tool = Figlet(font='eftipiti')
print(tool.renderText('Domain  Whois  Tool'))

ononemli = Figlet(font='digital')
print(ononemli.renderText('o n o n e m l i'))

sleep(0.5)
enterdomain = input("Enter domain name: ")

if enterdomain == '':
    input('\n''Press enter to exit')
    if input: exit()
else:
    domain_info = whois.whois(enterdomain)
    domain = domain_info.domain
    domain = str(domain)
    domain_name = domain_info.domain_name
    domain_name = str(domain_name)
    registrar = domain_info.registrar
    registrar = str(registrar)
    whois_server = domain_info.whois_server
    whois_server = str(whois_server)
    referral_url = domain_info.referral_url
    referral_url = str(referral_url)
    updated_date = domain_info.updated_date
    updated_date = str(updated_date)
    creation_date = domain_info.creation_date
    creation_date = str(creation_date)
    expiration_date = domain_info.expiration_date
    expiration_date = str(expiration_date)
    name_servers = domain_info.name_servers
    name_servers = str(name_servers)
    status = domain_info.status
    status = str(status)
    emails = domain_info.emails
    emails = str(emails)
    dnssec = domain_info.dnssec
    dnssec = str(dnssec)
    name = domain_info.name
    name = str(name)
    org = domain_info.org
    org = str(org)
    address = domain_info.address
    address = str(address)
    city = domain_info.city
    city = str(city)
    state = domain_info.state
    state = str(state)
    zipcode = domain_info.zipcode
    zipcode = str(zipcode)
    country = domain_info.country
    country = str(country)

    print('\n''Domain____________________:' '\t' +domain)
    print('Domain Name_______________:' '\t' +domain_name)
    print('Registrar_________________:' '\t' +registrar)
    print('Whois Server______________:' '\t' +whois_server)
    print('Referral URL______________:' '\t' +referral_url)
    print('Updated Date______________:' '\t' +updated_date)
    print('Creation Date_____________:' '\t' +creation_date)
    print('Expiration Date___________:' '\t' +expiration_date)
    print('\n''Name Servers______________:' '\t' +name_servers)
    print('\n''Status____________________:' '\t' +status)
    print('\n''Emails____________________:' '\t' +emails)
    print('DNS SEC___________________:' '\t' +dnssec)
    print('Name______________________:' '\t' +name)
    print('Org_______________________:' '\t' +org)
    print('Address___________________:' '\t' +address)
    print('City______________________:' '\t' +city)
    print('State_____________________:' '\t' +state)
    print('Zipcode___________________:' '\t' +zipcode)
    print('Country___________________:' '\t' +country)

    sleep(0.5)
    input('\n''Press enter to exit')
    if input: exit()