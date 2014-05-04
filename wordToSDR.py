import urllib2;
import json;

def createSDR(wordStr):
    ceptUrl = "http://api.cept.at/v1/term2bitmap";
    appIdParam = "app_id=0201d171";
    appKeyParam = "app_key=c15941581b95b92021d4ec61f00819c7";
    wordParam = "term=" + wordStr;
    andChar = "&";
    qstMark = "?";
    
    queryUrl = ceptUrl + qstMark + wordParam + andChar + appIdParam + andChar + appKeyParam;
    queryResult =json.loads(urllib2.urlopen(queryUrl).read());
    return queryResult['bitmap']
    
