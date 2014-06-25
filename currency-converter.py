a = raw_input('Enter currency to convert from?')
a = a.upper()

b = raw_input('Enter currency to convert to?')
b = b.upper()

c = float(raw_input('Enter value to convert?'))

url = ('http://rate-exchange.appspot.com/currency?from=%s&to=%s&q=1') % (a, b)
print url

urlalt = ('http://themoneyconverter.com/%s/%s.aspx') % (a, b)
print urlalt

#split and strip
split1 = (' : 1 %s = ') % a
strip1 = (' %s</h2>') % b
