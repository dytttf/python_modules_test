#coding:utf8
import urlparse
import urllib
from pprint import pprint
import base64

url = "http://www.baidu.com?a=1,2&b=3"

def get_all_query_ad_dict(url):
    url_parser = urlparse.urlparse(url)
    print dir(url_parser)
    query_dic = dict(urlparse.parse_qsl(url_parser.query))
    return query_dic

def re_build_url(ori_url, query_dic={}):
    data = urllib.urlencode(query_dic)
    url_parser = urlparse.urlparse(ori_url)
    url = urlparse.urlunparse((url_parser.scheme, url_parser.netloc, url_parser.path, url_parser.params, data, ""))
    return url

if __name__ == "__main__":
    url = 'https://www.wilsoncenter.org/views/ajax?ajax_html_ids%5B%5D=skip-link&ajax_html_ids%5B%5D=page-header&ajax_html_ids%5B%5D=block-views-exp-site-search-search-results&ajax_html_ids%5B%5D=views-exposed-form-site-search-search-results&ajax_html_ids%5B%5D=edit-search&ajax_html_ids%5B%5D=edit-submit-site-search&ajax_html_ids%5B%5D=nav&ajax_html_ids%5B%5D=main-content&ajax_html_ids%5B%5D=block-views-exp-section-search-events-past&ajax_html_ids%5B%5D=views-exposed-form-section-search-events-past&ajax_html_ids%5B%5D=edit-search&ajax_html_ids%5B%5D=edit-submit-section-search&ajax_html_ids%5B%5D=edit-topic&ajax_html_ids%5B%5D=edit-region&ajax_html_ids%5B%5D=month-october-2015&ajax_html_ids%5B%5D=node-37271&ajax_html_ids%5B%5D=node-37641&ajax_html_ids%5B%5D=node-35926&ajax_html_ids%5B%5D=node-37246&ajax_html_ids%5B%5D=node-37306&ajax_html_ids%5B%5D=node-37401&ajax_html_ids%5B%5D=node-36891&ajax_html_ids%5B%5D=node-37011&ajax_html_ids%5B%5D=node-37546&ajax_html_ids%5B%5D=node-37031&ajax_html_ids%5B%5D=node-37181&ajax_html_ids%5B%5D=node-36996&ajax_html_ids%5B%5D=node-37131&ajax_html_ids%5B%5D=node-36216&ajax_html_ids%5B%5D=node-36831&ajax_html_ids%5B%5D=node-37226&ajax_html_ids%5B%5D=node-36161&ajax_html_ids%5B%5D=node-36921&ajax_html_ids%5B%5D=node-36906&ajax_html_ids%5B%5D=node-36336&ajax_html_ids%5B%5D=node-36366&ajax_html_ids%5B%5D=node-36461&ajax_html_ids%5B%5D=node-37061&ajax_html_ids%5B%5D=node-36926&ajax_html_ids%5B%5D=node-36946&ajax_html_ids%5B%5D=node-35781&ajax_html_ids%5B%5D=node-36846&ajax_html_ids%5B%5D=node-36046&ajax_html_ids%5B%5D=node-35836&ajax_html_ids%5B%5D=node-36741&ajax_html_ids%5B%5D=node-36806&ajax_html_ids%5B%5D=node-36696&ajax_html_ids%5B%5D=node-35771&ajax_html_ids%5B%5D=node-36116&ajax_html_ids%5B%5D=node-36091&ajax_html_ids%5B%5D=node-36401&ajax_html_ids%5B%5D=block-wilsoncenter-blocks-contact&ajax_html_ids%5B%5D=block-wilsoncenter-blocks-donate&ajax_html_ids%5B%5D=block-wilsoncenter-blocks-email-updates&ajax_html_ids%5B%5D=wilsoncenter-blocks-newsletter-signup-form&ajax_html_ids%5B%5D=edit-email&ajax_html_ids%5B%5D=edit-submit&ajax_html_ids%5B%5D=footer-nav&ajax_html_ids%5B%5D=ui-id-2&ajax_html_ids%5B%5D=ui-id-1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.button.css%5D=1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.core.css%5D=1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.dialog.css%5D=1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.resizable.css%5D=1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.theme.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Ffield%2Ftheme%2Ffield.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fnode%2Fnode.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsearch%2Fsearch.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.base.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.menus.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.messages.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.theme.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fuser%2Fuser.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fcalendar%2Fcss%2Fcalendar_multiday.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fctools%2Fcss%2Fctools.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fdate%2Fdate_api%2Fdate.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fdate%2Fdate_popup%2Fthemes%2Fdatepicker.1.7.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews%2Fcss%2Fviews.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fcustom%2Fwilsoncenterpl%2Fbower_components%2Fmagnific-popup%2Fdist%2Fmagnific-popup.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fcustom%2Fwilsoncenterpl%2Fcss%2Fstyle.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fcustom%2Fwilsoncenterpl%2Fjquery.ui.core.min.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fcustom%2Fwilsoncenterpl%2Fjquery.ui.tabs.min.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fcustom%2Fwilsoncenterpl%2Fjquery.ui.theme.min.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fcustom%2Fwilsoncenterpl%2Fsystem.menus.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fcustom%2Fwilsoncenterpl%2Fsystem.theme.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Ffiles%2Fcss%2Ffollow.css%5D=1&ajax_page_state%5Bjquery_version%5D=1.10&ajax_page_state%5Bjs%5D%5B%2F%2Fuse.typekit.net%2Frjt0cou.js%5D=1&ajax_page_state%5Bjs%5D%5B0%5D=1&ajax_page_state%5Bjs%5D%5B1%5D=1&ajax_page_state%5Bjs%5D%5B2%5D=1&ajax_page_state%5Bjs%5D%5B3%5D=1&ajax_page_state%5Bjs%5D%5B4%5D=1&ajax_page_state%5Bjs%5D%5Bhttps%3A%2F%2Fsadmin.brightcove.com%2Fjs%2FBrightcoveExperiences.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fajax.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fdrupal.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fjquery.once.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fprogress.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fctools%2Fjs%2Fauto-submit.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fgoogle_analytics%2Fgoogleanalytics.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Fjs%2Fjquery_update.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Freplace%2Fjquery%2F1.10%2Fjquery.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Freplace%2Fmisc%2Fjquery.form.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Freplace%2Fui%2Fexternal%2Fjquery.cookie.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Freplace%2Fui%2Fui%2Fminified%2Fjquery.ui.button.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Freplace%2Fui%2Fui%2Fminified%2Fjquery.ui.core.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Freplace%2Fui%2Fui%2Fminified%2Fjquery.ui.dialog.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Freplace%2Fui%2Fui%2Fminified%2Fjquery.ui.draggable.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Freplace%2Fui%2Fui%2Fminified%2Fjquery.ui.mouse.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Freplace%2Fui%2Fui%2Fminified%2Fjquery.ui.position.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Freplace%2Fui%2Fui%2Fminified%2Fjquery.ui.resizable.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Freplace%2Fui%2Fui%2Fminified%2Fjquery.ui.widget.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews%2Fjs%2Fajax_view.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews%2Fjs%2Fbase.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews_load_more%2Fviews_load_more.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Fwilsoncenter_blocks%2Fjs%2Fwilsoncenter_blocks_newsletter_signup_form.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Fwilsoncenter_search%2Fjs%2Fwilsoncenter_search.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fcustom%2Fwilsoncenterpl%2Fbower_components%2Fimagesloaded%2Fimagesloaded.pkgd.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fcustom%2Fwilsoncenterpl%2Fbower_components%2Fisotope%2Fdist%2Fisotope.pkgd.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fcustom%2Fwilsoncenterpl%2Fbower_components%2Flodash%2Flodash.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fcustom%2Fwilsoncenterpl%2Fbower_components%2Fmagnific-popup%2Fdist%2Fjquery.magnific-popup.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fcustom%2Fwilsoncenterpl%2Fbower_components%2FmatchHeight%2Fjquery.matchHeight-min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fcustom%2Fwilsoncenterpl%2Fbower_components%2Fmodernizr%2Fmodernizr.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fcustom%2Fwilsoncenterpl%2Fbower_components%2Fsly%2Fdist%2Fsly.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fcustom%2Fwilsoncenterpl%2Fjs%2Fscript.js%5D=1&ajax_page_state%5Btheme%5D=wilsoncenterpl&ajax_page_state%5Btheme_token%5D=caIL1o0bamIM6tz4bH43mQ5UzDI3v0G3V8gyEH_rbGc&page=6&pager_element=0&region=All&topic=All&view_args=&view_base_path=events%2Fpast&view_display_id=events_past&view_dom_id=57f81d43e5dc8ab63e44d05b2a06d98a&view_name=section_search&view_path=events%2Fpast'
    url = "http://statis.api.3g.youku.com/openapi-wireless/statis/recall_push_service?pid=bb2388e929bc3038&guid=f5c5bedb529c8599480a68047479d493&mac=38%3Abc%3A1a%3A40%3A55%3A41&imei=867348023674182&ver=5.4.4&_t_=1457340687&e=md5&_s_=e45e8c4a5184b402a5adb1054df45e92&operator=CMCC_46000&network=WIFI&appname=com.youku.phone&type=2&businesstype=youku&ostype=android&unionname=youku&status=1"
    query_dic = get_all_query_ad_dict(url)
    #for k, v in query_dic.iteritems():
    #    print k, base64.decodestring(v)
    #    print k, v
    pprint(query_dic)
    dic = {  #'authToken': 'hHCK',
             #'authType': 'OPENLINK',
             'id': 'ADEAABgTc5MB46KtH4i0CMkxqLoWENSO0nhkaQU',
             #'locale': 'zh_TW',
             #'srchid': '4599614851447494796169',
             #'srchindex': '990',
             #'srchtotal': '11871095',
             #'trk': 'vsrp_people_res_photo',
             #'trkInfo': 'VSRPsearchId:4599614851447494796169,VSRPtargetId:403927955,VSRPcmpt:primary,VSRPnm:false,authType:OPENLINK'
             }
    url = re_build_url(url, dic)
    print url
