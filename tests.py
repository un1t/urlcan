from urlcan import canonicalize

def test_1():
    assert canonicalize("http://host/%25%32%35") == "http://host/%25"

def test_2():    
    assert canonicalize("http://host/%25%32%35%25%32%35") == "http://host/%25%25"

def test_3():
    assert canonicalize("http://host/%2525252525252525") == "http://host/%25"

def test_4():
    assert canonicalize("http://host/asdf%25%32%35asd") == "http://host/asdf%25asd"

def test_5():
    assert canonicalize("http://host/%%%25%32%35asd%%") == "http://host/%25%25%25asd%25%25"

def test_6():
    assert canonicalize("http://www.google.com/") == "http://www.google.com/"

def test_7():
    assert canonicalize("http://%31%36%38%2e%31%38%38%2e%39%39%2e%32%36/%2E%73%65%63%75%72%65/%77%77%77%2E%65%62%61%79%2E%63%6F%6D/") == "http://168.188.99.26/.secure/www.ebay.com/"

def test_8():
    assert canonicalize("http://195.127.0.11/uploads/%20%20%20%20/.verify/.eBaysecure=updateuserdataxplimnbqmn-xplmvalidateinfoswqpcmlx=hgplmcx/") == "http://195.127.0.11/uploads/%20%20%20%20/.verify/.eBaysecure=updateuserdataxplimnbqmn-xplmvalidateinfoswqpcmlx=hgplmcx/"

def test_9():
    assert canonicalize("http://host%23.com/%257Ea%2521b%2540c%2523d%2524e%25f%255E00%252611%252A22%252833%252944_55%252B") == "http://host%23.com/~a!b@c%23d$e%25f^00&11*22(33)44_55+"

def test_10():
    assert canonicalize("http://3279880203/blah") == "http://195.127.0.11/blah"

def test_11():
    assert canonicalize("http://www.google.com/blah/..") == "http://www.google.com/"

def test_12():
    assert canonicalize("www.google.com/") == "http://www.google.com/"

def test_13():
    assert canonicalize("www.google.com") == "http://www.google.com/"

def test_14():
    assert canonicalize("http://www.evil.com/blah#frag") == "http://www.evil.com/blah"

def test_15():
    assert canonicalize("http://www.GOOgle.com/") == "http://www.google.com/"

def test_16():
    assert canonicalize("http://www.google.com.../") == "http://www.google.com/"

def test_17():
    assert canonicalize("http://www.google.com/foo\tbar\rbaz\n2") == "http://www.google.com/foobarbaz2"

def test_18():
    assert canonicalize("http://www.google.com/q?") == "http://www.google.com/q?"

def test_19():
    assert canonicalize("http://www.google.com/q?r?") == "http://www.google.com/q?r?"

def test_20():
    assert canonicalize("http://www.google.com/q?r?s") == "http://www.google.com/q?r?s"

def test_21():
    assert canonicalize("http://evil.com/foo#bar#baz") == "http://evil.com/foo"

def test_22():
    assert canonicalize("http://evil.com/foo;") == "http://evil.com/foo;"

def test_23():
    assert canonicalize("http://evil.com/foo?bar;") == "http://evil.com/foo?bar;"

def test_24():
    assert canonicalize("http://\x01\x80.com/") == "http://%01%80.com/"

def test_25():
    assert canonicalize("http://notrailingslash.com") == "http://notrailingslash.com/"

def test_26():
    assert canonicalize("http://www.gotaport.com:1234/") == "http://www.gotaport.com:1234/"

def test_27():
    assert canonicalize("  http://www.google.com/  ") == "http://www.google.com/"

def test_28():
    assert canonicalize("http:// leadingspace.com/") == "http://%20leadingspace.com/"

def test_29():
    assert canonicalize("http://%20leadingspace.com/") == "http://%20leadingspace.com/"

def test_30():
    assert canonicalize("%20leadingspace.com/") == "http://%20leadingspace.com/"

def test_31():
    assert canonicalize("https://www.securesite.com/") == "https://www.securesite.com/"

def test_32():
    assert canonicalize("http://host.com/ab%23cd") == "http://host.com/ab%23cd"

def test_33():
    assert canonicalize("http://host.com//twoslashes?more//slashes") == "http://host.com/twoslashes?more//slashes"
