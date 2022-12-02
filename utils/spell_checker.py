from .sentence_cutting import cutting_500_under
import requests, json


def cleaned_result(final_result):
    result = []
    tmp = final_result.split('<br>')
    
    WRONG_SPELLING = "<span class='red_text'>"
    WRONG_SPACING = "<span class='green_text'>"
    AMBIGUOUS = "<span class='violet_text'>"
    STATISTICAL_CORRECTION = "<span class='blue_text'>"
        
    for idx in range(len(tmp)):
        tmp[idx] = tmp[idx].replace(WRONG_SPELLING,'<span style="color:#CC0000">')
        tmp[idx] = tmp[idx].replace(WRONG_SPACING,'<span style="color:#00CC00">')
        tmp[idx] = tmp[idx].replace(AMBIGUOUS,'<span style="color:#CC00CC">')
        tmp[idx] = tmp[idx].replace(STATISTICAL_CORRECTION,'<span style="color:#3B78FF">')
        tmp[idx] = tmp[idx].replace('&quot;','"').replace("&#39;","'")
        if "<span" not in tmp[idx]:
            tmp[idx] = f"<span>{tmp[idx]}</span>"
        result.append(tmp[idx])
        
    return result


def check(text):
    base_url = 'https://m.search.naver.com/p/csearch/ocontent/spellchecker.nhn'
    _agent = requests.Session()
    
    final_result = []
    
    if len(text) > 500:
        cutted_text = cutting_500_under(text)
        
        for sentence in cutted_text:
                tmp_result = []
                payload = {
                    '_callback': 'window.__jindo2_callback._spellingCheck_0',
                    'q': sentence
                }
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                    'referer': 'https://search.naver.com/',
                }
                r = _agent.get(base_url, params=payload, headers=headers)
                r = r.text[42:-2]
                data = json.loads(r)
                html = data['message']['result']['html']
                tmp_result.append(html)
                final_result.extend(tmp_result)
                
        return '<br>'.join(final_result)
                
    else:
        payload = {
            '_callback': 'window.__jindo2_callback._spellingCheck_0',
            'q': text
        }
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'referer': 'https://search.naver.com/',
        }
        r = _agent.get(base_url, params=payload, headers=headers)
        r = r.text[42:-2]
        data = json.loads(r)
        html = data['message']['result']['html']
        
        return html