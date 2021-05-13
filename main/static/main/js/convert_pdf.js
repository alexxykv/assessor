function redirect(first_name, last_name, patronymic, city, date_birth, phone_number, email, site_1, site_2, site_3,
                  site_4, site_5, site_6, site_7, site_8, site_9, site_10) {
    window.location = `result/convert?first_name=${first_name}&last_name=${last_name}&
    patronymic=${patronymic}&city=${city}&date_birth=${date_birth}&
    phone_number=${phone_number}&email=${email}&
    site_1=${site_1}&site_2=${site_2}&site_3=${site_3}&site_4=${site_4}&site_5=${site_5}&
    site_6=${site_6}&site_7=${site_7}&site_8=${site_8}&site_9=${site_9}&site_10=${site_10}`;
}