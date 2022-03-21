from faker import Faker

fake = Faker(locale='en_CA')

website = 'Advantage Online Shopping'
adv_url = 'https://advantageonlineshopping.com/#/'
adv_title = '\xa0Advantage Shopping'

# new_user
new_f_name = fake.first_name()
new_l_name = fake.last_name()
new_full_name = f'{new_f_name} {new_l_name}'
new_username = f'{(new_f_name + new_l_name).lower()[0:9]}'
new_email = f'{new_username}@tg.ca'
new_phone = fake.phone_number()
new_city = fake.city()
new_country = fake.current_country()
new_address = fake.street_address()
new_province = fake.province()[0:9]
new_postal_code = fake.postalcode()
new_password = fake.password(length=10, special_chars=True, upper_case=True, digits=True)

account_dict = {'usernameRegisterPage': new_username,
                'emailRegisterPage': new_email,
                'passwordRegisterPage': new_password,
                'confirm_passwordRegisterPage': new_password,
                'first_nameRegisterPage': new_f_name,
                'last_nameRegisterPage': new_l_name,
                'phone_numberRegisterPage': new_phone,
                'countryListboxRegisterPage': new_country,
                'cityRegisterPage': new_city,
                'addressRegisterPage': new_address,
                'state_/_province_/_regionRegisterPage': new_province,
                'postal_codeRegisterPage': new_postal_code}


class User:
    username = account_dict['usernameRegisterPage']
    email = account_dict['emailRegisterPage']
    password = account_dict['passwordRegisterPage']
    phone = account_dict['phone_numberRegisterPage']
    first_name = account_dict['first_nameRegisterPage']
    last_name = account_dict['last_nameRegisterPage']
    full_name = f'{first_name} {last_name}'


social_media = {"FACEBOOK": "follow_facebook", "TWITTER": "follow_twitter", "LINKEDIN": "follow_linkedin"}
texts = ["SPECIAL OFFER", "ALL YOU WANT FROM A TABLET", "POPULAR ITEMS", "FOLLOW US"]
links = ['TABLETS', 'SPEAKERS', 'LAPTOPS', 'MICE', 'HEADPHONES']
links_text = ['OUR PRODUCTS', 'SPECIAL OFFER', 'POPULAR ITEMS', 'CONTACT US']
