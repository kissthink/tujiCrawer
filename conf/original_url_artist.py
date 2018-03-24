#encoding:utf-8
webInfo = {
    'studentart.com.cn':{
        'category':'艺术', 
        'domain':'studentart.com.cn', 
        'sourceUrl':{
            'http://www.studentart.com.cn/arts/artwork?ptype=1&p=0':332,
            'http://www.studentart.com.cn/arts/artwork?ptype=2&p=0':778,
            'http://www.studentart.com.cn/arts/artwork?ptype=3&p=0':75,
            'http://www.studentart.com.cn/arts/artwork?ptype=6&p=0':85,
            'http://www.studentart.com.cn/arts/artwork?ptype=4&p=0':5,
            'http://www.studentart.com.cn/arts/artwork?ptype=9&p=0':60,
            'http://www.studentart.com.cn/arts/artwork?ptype=10&p=0':107,
        },
        'urlPattern':'http://www.studentart.com.cn/arts/artwork/detail/\d+',
        'fenyePattern':['p=0', 'p=%d'],
        'titleXpath':'//h1/text()',
        'textPattern':{"tag":"div", "class":["artworks_infol"]},
        'bodyPattern':{"tag":"img", "id":["smallimg"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },

    'artso.artron.net':{
        'category':'艺术', 
        'domain':'artso.artron.net', 
        'sourceUrl':{
            'http://artso.artron.net/jewel/search_jewel.php?oneClass=800000&page=1':3188,
            'http://artso.artron.net/jewel/search_jewel.php?oneClass=180000&page=1':966,
            'http://artso.artron.net/jewel/search_jewel.php?oneClass=700000&page=1':6250,
            'http://artso.artron.net/jewel/search_jewel.php?oneClass=170000&page=1':1574,
            'http://artso.artron.net/jewel/search_jewel.php?oneClass=400000&page=1':447,
        },
        'urlPattern':'http://gallery.artron.net/works/.*\d+.html',
        'fenyePattern':['page=1', 'page=%d'],
        'titleXpath':'//h1/text()',
        'textPattern':{"tag":"table", "class":["table"]},
        'bodyPattern':{"tag":"div", "id":["smallPic"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },

    'artist.artxun.com':{
        'category':'艺术', 
        'domain':'artist.artxun.com', 
        'sourceUrl':{
            'http://artist.artxun.com/opus/1/':334,
            'http://artist.artxun.com/opus/zhongguohua/1/':334,
            'http://artist.artxun.com/opus/shufazuopin/1/':334,
            'http://artist.artxun.com/opus/mingjiashufa/1/':302,
            'http://artist.artxun.com/opus/hengfu/1/':112,
            'http://artist.artxun.com/opus/shufu/1/':42,
            'http://artist.artxun.com/opus/yingbishufa/1/':86,
            'http://artist.artxun.com/opus/zhongguoyouhua/1/':322,
            'http://artist.artxun.com/opus/fengjinyouhua/1/':190,
            'http://artist.artxun.com/opus/shanshuifengjin/1/':51,
            'http://artist.artxun.com/opus/renwuyouhua/1/':162,
            'http://artist.artxun.com/opus/huahuiyouhua/1/':11,
            'http://artist.artxun.com/opus/dongwuyouhua/1/':23,
            'http://artist.artxun.com/opus/jinwuyouhua/1/':61,
            'http://artist.artxun.com/opus/minjiaguohua/1/':334,
            'http://artist.artxun.com/opus/minjiarenwu/1/':191,
            'http://artist.artxun.com/opus/minjiahuaniao/1/':202,
            'http://artist.artxun.com/opus/minjiashanshui/1/':209,
        },
        'urlPattern':'http://mall.artxun.com/goods-\d+.html',
        'fenyePattern':['/1/', '/%d/'],
        'titleXpath':'//h1/text()',
        'textPattern':{"tag":"ul", "class":["product_list_ul"]},
        'bodyPattern':{"tag":"div", "class":["zoom-desc"]},
        'imgReplace':[['&amp;type=gallery&amp;h=75&amp;w=75', '&type=gallery&h=-1&w=-1']],
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http://imgmall.artxun.com/img.php.{0,50}75',
        'isAlbum':1
    },

    'tuku.cn': {
        'category': '艺术',
        'domain': 'tuku.cn',
        'sourceUrl': {
            'http://www.tuku.cn/aclass.aspx?id=4&Page=1':4,
        },
        'urlPattern': 'http://www.tuku.cn/.*typeid=\d+',
        'bodyPattern': {'tag': 'from','id': ['form1']},'imgPattern': u'(?is)(<img.*?>)',
        'fenyePattern': ['Page=1', 'Page=%d'],
        'imgUrlPattern': u'http://image5.tuku.cn/pic/.*/s\d+.(jpg|jpeg)',
        'detailFenyePattern': ['', '&Page=%d'],
        'imgReplace': [['/s0', '/0'], ['/s1', '/1'], ['/s2', '/2'], ['/s3', '/3'], ['/s4', '/4'], ['/s5', '/5']],
        'isAlbum': 1
    },

    'taopic.com':{
        'category':'艺术',
        'domain':'taopic.com',
        'sourceUrl':{
            'http://www.taopic.com/tuku/shuhuawenzi/list_1.html': 209,
            'http://www.taopic.com/tuku/jianzhiyishu/list_1.html': 8,
        },
        'urlPattern':'http://www.taopic.com/tuku/\d+/\d+.html',
        'fenyePattern':['1.html', '%d.html'],
        'bodyPattern':{"tag":"div", "class":["viewBoxPad"]},
        'myposPattern': {"tag":"div", "class":["crumbs"]},
        'textPattern': {"tag":"div", "class":["viewBoxPad"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },

     'sns.91ddcc.com':{
         'category':'艺术',
         'domain':'sns.91ddcc.com',
         'sourceUrl':{
                 'https://sns.91ddcc.com/stage/cate-4-0-1':17,
                 'https://sns.91ddcc.com/stage/cate-12-0-1':15,
                 'https://sns.91ddcc.com/stage/cate-3-0-1':8,
                 'https://sns.91ddcc.com/stage/cate-8-0-1':20,
             },
         'sourcePattern':'https://sns.91ddcc.com/s/\d+',
         'sourceFenyePattern':['','?p=%d&g=0'],
         'urlPattern':'https://sns.91ddcc.com/t/\d+',
         'fenyePattern':['-0-1', '-0-%d'],
         'bodyPattern':{"tag":"div", "class":["tz_p"]},
         #'myposPattern': {"tag":"div", "class":["tz_more"]},
         'myposXpath':'//div[@class="tz_more"]/div/p[1]/text()',
         #'textXpath':'//div[@class="article-con"]/p/text()',
         'imgPattern':ur'(?is)(<img.*?>)',
         'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
         'isAlbum':1
        },

     'zhsh5000.com':{
         'category':'艺术',
         'domain':'zhsh5000.com',
         'sourceUrl':{
                 'http://www.zhsh5000.com/ysz.asp?classid=15&page=1':5135,
                 'http://www.zhsh5000.com/newslist.asp?bclassid=2&page=1':23,
             },
         'urlPattern':'http://www.zhsh5000.com/((productinfo.asp?id=\d+)|(news.asp?bclassid=2&id=\d+))',
         'fenyePattern':['[page=1', 'page=%d'],
         'titleXpath':'//h1[@class="newdd"]/text()',
         'myposXpath':'//td[@class="td06"]/text()',
         'contentXpath':'//div[@class="newddz"]/p/text()',
         'imgXpath':'//div[@class="newddz"]/font/p/@src',
         'isAlbum':0
        },

    'tjculture.com':{
        'category':'艺术',
        'domain':'tjculture.com',
        'sourceUrl':{
                'http://www.tjculture.com/list.php?class=9&page=1':297,
            },
        'urlPattern':'http://www.tjculture.com/list/\d+/\d+_\d+.html',
        'fenyePattern':['page=1', 'page=%d'],
        'bodyPattern':{"tag":"div", "class":["news_subject"]},
        'myposPattern': {"tag":"div", "class":["rightpic"]},
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*?\.(jpg|jpeg|JPG|png)',
        #'imgReplace':[['img.zhuoku.com','bizhi.zhuoku.com']],
        'textXpath':'//div[@class="news_title"]/strong/text()',
	    'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

    'myyishu.com':{ 
        'category':'艺术', 
        'domain':'myyishu.com',
        'sourceUrl':{
                'http://www.myyishu.com/artwork/c1013.html?cpa=1':106,
                'http://www.myyishu.com/artwork/c1014.html?cpa=1':38,
                'http://www.myyishu.com/artwork/c1015.html?cpa=1':112,
                'http://www.myyishu.com/artwork/c1016.html?cpa=1':9,
                'http://www.myyishu.com/artwork/c1017.html?cpa=1':5,
                'http://www.myyishu.com/artwork/c1018.html?cpa=1':9,
            },
        'urlPattern':'http://www.myyishu.com:80/artwork/\d+.html',
        'fenyePattern':['cpa=1', 'cpa=%d'],
        'bodyPattern':{"tag":"div", "class":["zoom-small-image"]},
        #'myposPattern': {"tag":"div", "class":["location"]},
        'myposXpath':'//div[@class="pageWrapper"]/div/a/text()',
        'textXpath':'//div[@class="pt5"]/b/text()',
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'imgReplace':[['_z.jpg','.jpg']],
        #'detailFenyePattern':['.html', '_%d.html'],
        'isAlbum':1
    },

    'artwork.myyishu.com':{
        'category':'艺术',
        'domain':'artwork.myyishu.com',
        'sourceUrl':{
                'http://www.myyishu.com/artwork/10-0-0-0-0-0-0-0-0-1.html':134,
                'http://www.myyishu.com/artwork/15-0-0-0-0-0-0-0-0-1.html':27,
                'http://www.myyishu.com/artwork/21-0-0-0-0-0-0-0-0-1.html':83,
                'http://www.myyishu.com/artwork/27-0-0-0-0-0-0-0-0-1.html':2,
            },
        'urlPattern':'http://www.myyishu.com/artwork/\d+.html',
        'bodyPattern':{"tag":"div", "class":["zoom-small-image"]},
        #'myposPattern': {"tag":"div", "class":["location"]},
        'myposXpath':'//div[@class="pageWrapper mainWrapper"]/div/a/text()',
        'textXpath':'//div[@class="pt5"]/b/text()',
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*\.(jpg|jpeg|gif|JPG|png)',
        'imgReplace':[['_z.jpg','.jpg']],
        #'detailFenyePattern':['.html', '_%d.html'],
        'fenyePattern':['1.html', '%d.html'],
        'isAlbum':1
    },

    'ivsky.com':{
        'category':'艺术',
        'domain':'ivsky.com',
        'sourceUrl':{
                'http://www.ivsky.com/tupian/shijieminghua_t19632/index_1.html':34,
                'http://www.ivsky.com/tupian/guohua_t5167/index_1.html':43,
                'http://www.ivsky.com/tupian/banhua_t1382/index_1.html':2,
                'http://www.ivsky.com/tupian/youhua_t2977/index_1.html':74,
                'http://www.ivsky.com/tupian/shuicaihua_t19633/index_1.html':16,
                'http://www.ivsky.com/tupian/shuimohua_t675/index_1.html':58,
                'http://www.ivsky.com/tupian/sumiao_t2406/index_1.html':13,
                'http://www.ivsky.com/tupian/gongbihua_t3235/index_1.html':16,
                'http://www.ivsky.com/tupian/zhidiao_t15553/index_1.html':6,
                'http://www.ivsky.com/tupian/minjianyishu_t19634/index_1.html':21,
                'http://www.ivsky.com/tupian/piying_t5812/index_1.html':2,
                'http://www.ivsky.com/tupian/jianzhi_t2789/index_1.html':49,
                'http://www.ivsky.com/tupian/lianpu_t4052/index_1.html':18,
                'http://www.ivsky.com/tupian/shufa_t5315/index_1.html':10,
                'http://www.ivsky.com/tupian/huihua_t2526/index_1.html':161,
                'http://www.ivsky.com/tupian/zhongguonianhua_t19636/index_1.html':6,
            },
        'fenyePattern':['1.html', '%d.html'],
        'urlPattern':'http://www.ivsky.com/tupian/.*?\d+/pic_\d+.html',
        'myposPattern': {"tag":"div", "class":["pos"]},
        'bodyPattern':{"tag":"div", "id":["pic_con"]},
        'textPattern':{"tag":"div", "class":["al_tit"]},
        #'textXpath':'//div[@class="text_wrap"]/h2/a/text()',
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*?\.(jpg|jpeg|gif|JPG|png)',
        'isAlbum':1
    },

    'yishu.ivsky.com':{
        'category':'艺术',
        'domain':'yishu.ivsky.com',
        'sourceUrl':{
                'http://www.ivsky.com/tupian/yishu/index_1.html':16,
            },  
        'fenyePattern':['1.html', '%d.html'],
        'urlPattern':'http://www.ivsky.com/tupian/.*?\d+/',
        'myposPattern': {"tag":"div", "class":["pos"]},
        'bodyPattern':{"tag":"ul", "class":["pli"]},
        'textPattern':{"tag":"div", "class":["al_tit"]},
        #'textXpath':'//div[@class="text_wrap"]/h2/a/text()',
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*?\.(jpg|jpeg|gif|JPG|png)',
        'imgReplace':[['/t/','/pre/']],
        'detailFenyePattern':['', 'index_%d.html'],
        'isAlbum':1
    },  

    'sootuu.com':{
        'category':'艺术',
        'domain':'sootuu.com',
        'sourceUrl':{
                'http://www.sootuu.com/photo/65/573/photo_573_1.html':50,
                'http://www.sootuu.com/photo/65/573/920/photo_920_1.html':40,
                'http://www.sootuu.com/photo/65/573/921/photo_921_1.html':7,
                'http://www.sootuu.com/photo/65/573/924/photo_924_1.html':20,
                'http://www.sootuu.com/photo/65/573/927/photo_927_1.html':3,
                'http://www.sootuu.com/photo/65/573/928/photo_928_1.html':12,
            },
        'fenyePattern':['1.html', '%d.html'],
        'urlPattern':'http://www.sootuu.com/photo/65/573/(920|921|924|927|928)/\d+/\d+/\d+.html',
        'myposPattern': {"tag":"p", "class":["tips_left"]},
        'bodyPattern':{"tag":"div", "class":["content_pic"]},
        'textXpath':'//div[@class="content_l_ul"]/h1/text()',
        'imgPattern':ur'(?is)(<img.*?>)',
        'imgUrlPattern':'http.*?\.(jpg|jpeg|gif|JPG|png)',
        #'imgReplace':[['_100.jpg','']],
        'isAlbum':1
    }, 

}
