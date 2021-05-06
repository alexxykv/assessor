async function PDF() {
    document.getElementById('pdf').remove();
    document.querySelector('.spinner-border').style.display = 'inline-block';;
    let convertApi = ConvertApi.auth({secret: 'pAmCFow1GShAOljX'});
    let params = convertApi.createParams();
    params.add('file', new URL('http://84.201.152.104:8000'));
    let result = await convertApi.convert('html', 'pdf', params);
    let url = result.files[0].Url;
    document.querySelector('.spinner-border').remove();
    document.getElementById('download').innerHTML = `<a href="${url}">Скачать</a>`;
}
