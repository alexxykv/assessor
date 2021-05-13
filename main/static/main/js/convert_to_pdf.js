async function PDF(first_name, last_name, patronymic, city, date_birth, phone_number, email, site_1, site_2, site_3,
                   site_4, site_5, site_6, site_7, site_8, site_9, site_10) {
    document.getElementById('pdf').remove();
    document.querySelector('.spinner-border').style.display = 'inline-block';
    let convertApi = ConvertApi.auth({secret: 'pAmCFow1GShAOljX'});
    let params = convertApi.createParams();
    params.add('file', new URL(`http://84.201.152.104:8000/result?first_name=${first_name}&last_name=${last_name}&
    patronymic=${patronymic}&city=${city}&date_birth=${date_birth}&
    phone_number=${phone_number}&email=${email}&
    site_1=${site_1}&site_2=${site_2}&site_3=${site_3}&site_4=${site_4}&site_5=${site_5}&
    site_6=${site_6}&site_7=${site_7}&site_8=${site_8}&site_9=${site_9}&site_10=${site_10}&  
    `));
    let result = await convertApi.convert('html', 'pdf', params);
    let url = result.files[0].Url;
    document.querySelector('.spinner-border').remove();
    document.getElementById('download').innerHTML = `http://84.201.152.104:8000/result?first_name=${first_name}&last_name=${last_name}&
    patronymic=${patronymic}&city=${city}&date_birth=${date_birth}&
    phone_number=${phone_number}&email=${email}&
    site_1=${site_1}&site_2=${site_2}&site_3=${site_3}&site_4=${site_4}&site_5=${site_5}&
    site_6=${site_6}&site_7=${site_7}&site_8=${site_8}&site_9=${site_9}&site_10=${site_10}`;
}