from faker import Faker

fake = Faker(locale='en_CA')

website = 'Advantage Online Shopping'
adv_url = 'https://advantageonlineshopping.com/#/'
adv_title = '\xa0Advantage Shopping'

# new_user
f_name = fake.first_name()
l_name = fake.last_name()
username = f'{(f_name + l_name[0:1]).lower()}'
email = f'{username}@tg.ca'
phone = fake.phone_number()
city = fake.city()
country = fake.current_country()
address = fake.street_address()
province = fake.province()[0:9]
postal_code = fake.postalcode()
password = fake.password(length=10, special_chars=True, upper_case=True, digits=True)

account_dict = {'usernameRegisterPage': username,
                'emailRegisterPage': email,
                'passwordRegisterPage': password,
                'confirm_passwordRegisterPage': password,
                'first_nameRegisterPage': f_name,
                'last_nameRegisterPage': l_name,
                'phone_numberRegisterPage': phone,
                'countryListboxRegisterPage': country,
                'cityRegisterPage': city,
                'addressRegisterPage': address,
                'state_/_province_/_regionRegisterPage': province,
                'postal_codeRegisterPage': postal_code}
