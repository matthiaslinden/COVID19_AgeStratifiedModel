#!/usr/bin/env python3.7
#coding:utf-8

import pandas as pd

class Landkreise(object):
    def __init__(self):
        self.lkrCodes = {8315: 'DE13', 8316: 'DE13', 8311: 'DE13', 8335: 'DE13', 8336: 'DE13', 8317: 'DE13', 8325: 'DE13', 8326: 'DE13', 8327: 'DE13', 8337: 'DE13', 8211: 'DE12', 8235: 'DE12', 8236: 'DE12', 8237: 'DE12', 8221: 'DE12', 8212: 'DE12', 8215: 'DE12', 8222: 'DE12', 8225: 'DE12', 8231: 'DE12', 8216: 'DE12', 8226: 'DE12', 8115: 'DE11', 8116: 'DE11', 8117: 'DE11', 8135: 'DE11', 8121: 'DE11', 8125: 'DE11', 8126: 'DE11', 8118: 'DE11', 8128: 'DE11', 8136: 'DE11', 8119: 'DE11', 8127: 'DE11', 8111: 'DE11', 8425: 'DE14', 8426: 'DE14', 8435: 'DE14', 8436: 'DE14', 8415: 'DE14', 8437: 'DE14', 8416: 'DE14', 8421: 'DE14', 8417: 'DE14', 9561: 'DE25', 9571: 'DE25', 9562: 'DE25', 9572: 'DE25', 9563: 'DE25', 9573: 'DE25', 9575: 'DE25', 9564: 'DE25', 9574: 'DE25', 9576: 'DE25', 9565: 'DE25', 9577: 'DE25', 9271: 'DE22', 9279: 'DE22', 9272: 'DE22', 9273: 'DE22', 9261: 'DE22', 9274: 'DE22', 9262: 'DE22', 9275: 'DE22', 9276: 'DE22', 9277: 'DE22', 9263: 'DE22', 9278: 'DE22', 9171: 'DE21', 9173: 'DE21', 9172: 'DE21', 9174: 'DE21', 9175: 'DE21', 9176: 'DE21', 9177: 'DE21', 9178: 'DE21', 9179: 'DE21', 9180: 'DE21', 9161: 'DE21', 9181: 'DE21', 9182: 'DE21', 9183: 'DE21', 9162: 'DE21', 9184: 'DE21', 9185: 'DE21', 9186: 'DE21', 9163: 'DE21', 9187: 'DE21', 9188: 'DE21', 9189: 'DE21', 9190: 'DE21', 9461: 'DE24', 9471: 'DE24', 9462: 'DE24', 9472: 'DE24', 9463: 'DE24', 9473: 'DE24', 9474: 'DE24', 9464: 'DE24', 9475: 'DE24', 9476: 'DE24', 9477: 'DE24', 9478: 'DE24', 9479: 'DE24', 9361: 'DE23', 9371: 'DE23', 9372: 'DE23', 9373: 'DE23', 9374: 'DE23', 9362: 'DE23', 9375: 'DE23', 9376: 'DE23', 9377: 'DE23', 9363: 'DE23', 9771: 'DE27', 9761: 'DE27', 9772: 'DE27', 9773: 'DE27', 9779: 'DE27', 9774: 'DE27', 9762: 'DE27', 9763: 'DE27', 9776: 'DE27', 9764: 'DE27', 9775: 'DE27', 9780: 'DE27', 9777: 'DE27', 9778: 'DE27', 9661: 'DE26', 9671: 'DE26', 9672: 'DE26', 9674: 'DE26', 9675: 'DE26', 9677: 'DE26', 9676: 'DE26', 9673: 'DE26', 9662: 'DE26', 9678: 'DE26', 9663: 'DE26', 9679: 'DE26', 11004: 'DE30', 11002: 'DE30', 11011: 'DE30', 11010: 'DE30', 11001: 'DE30', 11008: 'DE30', 11003: 'DE30', 11012: 'DE30', 11005: 'DE30', 11006: 'DE30', 11007: 'DE30', 11009: 'DE30', 12060: 'DE40', 12051: 'DE40', 12052: 'DE40', 12061: 'DE40', 12062: 'DE40', 12053: 'DE40', 12063: 'DE40', 12064: 'DE40', 12065: 'DE40', 12066: 'DE40', 12067: 'DE40', 12068: 'DE40', 12054: 'DE40', 12069: 'DE40', 12070: 'DE40', 12071: 'DE40', 12072: 'DE40', 12073: 'DE40', 4011: 'DE50', 4012: 'DE50', 2000: 'DE60', 6431: 'DE71', 6411: 'DE71', 6432: 'DE71', 6412: 'DE71', 6433: 'DE71', 6434: 'DE71', 6435: 'DE71', 6436: 'DE71', 6437: 'DE71', 6413: 'DE71', 6438: 'DE71', 6439: 'DE71', 6440: 'DE71', 6414: 'DE71', 6531: 'DE72', 6532: 'DE72', 6533: 'DE72', 6534: 'DE72', 6535: 'DE72', 6631: 'DE73', 6632: 'DE73', 6611: 'DE73', 6633: 'DE73', 6634: 'DE73', 6635: 'DE73', 6636: 'DE73', 13076: 'DE80', 13071: 'DE80', 13074: 'DE80', 13003: 'DE80', 13072: 'DE80', 13004: 'DE80', 13075: 'DE80', 13073: 'DE80', 3101: 'DE91', 3151: 'DE91', 3153: 'DE91', 3159: 'DE91', 3154: 'DE91', 3155: 'DE91', 3157: 'DE91', 3102: 'DE91', 3158: 'DE91', 3103: 'DE91', 3251: 'DE92', 3252: 'DE92', 3241: 'DE92', 3254: 'DE92', 3255: 'DE92', 3256: 'DE92', 3257: 'DE92', 3351: 'DE93', 3352: 'DE93', 3353: 'DE93', 3358: 'DE93', 3354: 'DE93', 3355: 'DE93', 3356: 'DE93', 3357: 'DE93', 3359: 'DE93', 3360: 'DE93', 3361: 'DE93', 3451: 'DE94', 3452: 'DE94', 3453: 'DE94', 3401: 'DE94', 3402: 'DE94', 3454: 'DE94', 3455: 'DE94', 3456: 'DE94', 3457: 'DE94', 3403: 'DE94', 3458: 'DE94', 3404: 'DE94', 3459: 'DE94', 3460: 'DE94', 3461: 'DE94', 3405: 'DE94', 3462: 'DE94', 5911: 'DEA5', 5913: 'DEA5', 5954: 'DEA5', 5914: 'DEA5', 5915: 'DEA5', 5916: 'DEA5', 5958: 'DEA5', 5962: 'DEA5', 5966: 'DEA5', 5970: 'DEA5', 5974: 'DEA5', 5978: 'DEA5', 5711: 'DEA4', 5754: 'DEA4', 5758: 'DEA4', 5762: 'DEA4', 5766: 'DEA4', 5770: 'DEA4', 5774: 'DEA4', 5112: 'DEA1', 5111: 'DEA1', 5113: 'DEA1', 5154: 'DEA1', 5114: 'DEA1', 5158: 'DEA1', 5116: 'DEA1', 5117: 'DEA1', 5119: 'DEA1', 5120: 'DEA1', 5162: 'DEA1', 5122: 'DEA1', 5166: 'DEA1', 5170: 'DEA1', 5124: 'DEA1', 5334: 'DEA2', 5314: 'DEA2', 5358: 'DEA2', 5366: 'DEA2', 5370: 'DEA2', 5315: 'DEA2', 5316: 'DEA2', 5374: 'DEA2', 5362: 'DEA2', 5378: 'DEA2', 5382: 'DEA2', 5554: 'DEA3', 5512: 'DEA3', 5558: 'DEA3', 5513: 'DEA3', 5515: 'DEA3', 5562: 'DEA3', 5566: 'DEA3', 5570: 'DEA3', 7131: 'DEB1', 7132: 'DEB1', 7133: 'DEB1', 7134: 'DEB1', 7135: 'DEB1', 7111: 'DEB1', 7137: 'DEB1', 7138: 'DEB1', 7140: 'DEB1', 7141: 'DEB1', 7143: 'DEB1', 7331: 'DEB3', 7332: 'DEB3', 7333: 'DEB3', 7311: 'DEB3', 7334: 'DEB3', 7312: 'DEB3', 7335: 'DEB3', 7336: 'DEB3', 7313: 'DEB3', 7314: 'DEB3', 7315: 'DEB3', 7339: 'DEB3', 7316: 'DEB3', 7317: 'DEB3', 7338: 'DEB3', 7318: 'DEB3', 7337: 'DEB3', 7340: 'DEB3', 7319: 'DEB3', 7320: 'DEB3', 7231: 'DEB2', 7232: 'DEB2', 7211: 'DEB2', 7235: 'DEB2', 7233: 'DEB2', 10042: 'DEC0', 10043: 'DEC0', 10044: 'DEC0', 10045: 'DEC0', 10046: 'DEC0', 10041: 'DEC0', 14511: 'DED4', 14521: 'DED4', 14522: 'DED4', 14523: 'DED4', 14524: 'DED4', 14625: 'DED2', 14612: 'DED2', 14626: 'DED2', 14627: 'DED2', 14628: 'DED2', 14713: 'DED5', 14729: 'DED5', 14730: 'DED5', 15081: 'DEE0', 15082: 'DEE0', 15083: 'DEE0', 15084: 'DEE0', 15001: 'DEE0', 15002: 'DEE0', 15085: 'DEE0', 15086: 'DEE0', 15003: 'DEE0', 15087: 'DEE0', 15088: 'DEE0', 15089: 'DEE0', 15090: 'DEE0', 15091: 'DEE0', 1051: 'DEF0', 1001: 'DEF0', 1053: 'DEF0', 1002: 'DEF0', 1003: 'DEF0', 1004: 'DEF0', 1054: 'DEF0', 1055: 'DEF0', 1056: 'DEF0', 1057: 'DEF0', 1058: 'DEF0', 1059: 'DEF0', 1060: 'DEF0', 1061: 'DEF0', 1062: 'DEF0', 16077: 'DEG0', 16061: 'DEG0', 16056: 'DEG0', 16051: 'DEG0', 16052: 'DEG0', 16067: 'DEG0', 16076: 'DEG0', 16069: 'DEG0', 16070: 'DEG0', 16053: 'DEG0', 16065: 'DEG0', 16062: 'DEG0', 16074: 'DEG0', 16075: 'DEG0', 16073: 'DEG0', 16066: 'DEG0', 16068: 'DEG0', 16072: 'DEG0', 16054: 'DEG0', 16064: 'DEG0', 16063: 'DEG0', 16055: 'DEG0', 16071: 'DEG0'}
        
        # Read Inhabitants of Landkreise from risklayer source
     #   kdf = pd.read_csv("risklayer_kreise.csv",header=[1,2])
     #   kdf = kdf[["AGS","Name","Einwohner"]]
     #   kdfID = kdf[["AGS","Einwohner"]]

     #   lkrN = dict(kdfID.values)
      #  for k,v in lkrN.items():
      #      lkrN[k] = int(v.replace(".",""))

        # Add Berlin's "Bezirke" manually 2019 numbers from wikipedia
    #    lkrN[11001] = 385748
    #    lkrN[11002] = 290386
    #    lkrN[11003] = 409335
    #    lkrN[11004] = 343592
    #    lkrN[11005] = 245197
    #    lkrN[11006] = 310071
    #    lkrN[11007] = 350984
    #    lkrN[11008] = 329917
    #    lkrN[11009] = 273689
    #    lkrN[11010] = 269967
    #    lkrN[11011] = 294201
    #    lkrN[11012] = 266408
    
        self.lkrNames = {1001: 'SK Flensburg', 1002: 'SK Kiel', 1003: 'SK Lübeck', 1004: 'SK Neumünster', 1051: 'LK Dithmarschen', 1053: 'LK Herzogtum Lauenburg', 1054: 'LK Nordfriesland', 1055: 'LK Ostholstein', 1056: 'LK Pinneberg', 1057: 'LK Plön', 1058: 'LK Rendsburg-Eckernförde', 1059: 'LK Schleswig-Flensburg', 1060: 'LK Segeberg', 1061: 'LK Steinburg', 1062: 'LK Stormarn', 2000: 'SK Hamburg', 3101: 'SK Braunschweig', 3102: 'SK Salzgitter', 3103: 'SK Wolfsburg', 3151: 'LK Gifhorn', 3153: 'LK Goslar', 3154: 'LK Helmstedt', 3155: 'LK Northeim', 3157: 'LK Peine', 3158: 'LK Wolfenbüttel', 3159: 'LK Göttingen', 3241: 'Region Hannover', 3251: 'LK Diepholz', 3252: 'LK Hameln-Pyrmont', 3254: 'LK Hildesheim', 3255: 'LK Holzminden', 3256: 'LK Nienburg (Weser)', 3257: 'LK Schaumburg', 3351: 'LK Celle', 3352: 'LK Cuxhaven', 3353: 'LK Harburg', 3354: 'LK Lüchow-Dannenberg', 3355: 'LK Lüneburg', 3356: 'LK Osterholz', 3357: 'LK Rotenburg (Wümme)', 3358: 'LK Heidekreis', 3359: 'LK Stade', 3360: 'LK Uelzen', 3361: 'LK Verden', 3401: 'SK Delmenhorst', 3402: 'SK Emden', 3403: 'SK Oldenburg', 3404: 'SK Osnabrück', 3405: 'SK Wilhelmshaven', 3451: 'LK Ammerland', 3452: 'LK Aurich', 3453: 'LK Cloppenburg', 3454: 'LK Emsland', 3455: 'LK Friesland', 3456: 'LK Grafschaft Bentheim', 3457: 'LK Leer', 3458: 'LK Oldenburg', 3459: 'LK Osnabrück', 3460: 'LK Vechta', 3461: 'LK Wesermarsch', 3462: 'LK Wittmund', 4011: 'SK Bremen', 4012: 'SK Bremerhaven', 5111: 'SK Düsseldorf', 5112: 'SK Duisburg', 5113: 'SK Essen', 5114: 'SK Krefeld', 5116: 'SK Mönchengladbach', 5117: 'SK Mülheim a.d.Ruhr', 5119: 'SK Oberhausen', 5120: 'SK Remscheid', 5122: 'SK Solingen', 5124: 'SK Wuppertal', 5154: 'LK Kleve', 5158: 'LK Mettmann', 5162: 'LK Rhein-Kreis Neuss', 5166: 'LK Viersen', 5170: 'LK Wesel', 5314: 'SK Bonn', 5315: 'SK Köln', 5316: 'SK Leverkusen', 5334: 'StadtRegion Aachen', 5358: 'LK Düren', 5362: 'LK Rhein-Erft-Kreis', 5366: 'LK Euskirchen', 5370: 'LK Heinsberg', 5374: 'LK Oberbergischer Kreis', 5378: 'LK Rheinisch-Bergischer Kreis', 5382: 'LK Rhein-Sieg-Kreis', 5512: 'SK Bottrop', 5513: 'SK Gelsenkirchen', 5515: 'SK Münster', 5554: 'LK Borken', 5558: 'LK Coesfeld', 5562: 'LK Recklinghausen', 5566: 'LK Steinfurt', 5570: 'LK Warendorf', 5711: 'SK Bielefeld', 5754: 'LK Gütersloh', 5758: 'LK Herford', 5762: 'LK Höxter', 5766: 'LK Lippe', 5770: 'LK Minden-Lübbecke', 5774: 'LK Paderborn', 5911: 'SK Bochum', 5913: 'SK Dortmund', 5914: 'SK Hagen', 5915: 'SK Hamm', 5916: 'SK Herne', 5954: 'LK Ennepe-Ruhr-Kreis', 5958: 'LK Hochsauerlandkreis', 5962: 'LK Märkischer Kreis', 5966: 'LK Olpe', 5970: 'LK Siegen-Wittgenstein', 5974: 'LK Soest', 5978: 'LK Unna', 6411: 'SK Darmstadt', 6412: 'SK Frankfurt am Main', 6413: 'SK Offenbach', 6414: 'SK Wiesbaden', 6431: 'LK Bergstraße', 6432: 'LK Darmstadt-Dieburg', 6433: 'LK Groß-Gerau', 6434: 'LK Hochtaunuskreis', 6435: 'LK Main-Kinzig-Kreis', 6436: 'LK Main-Taunus-Kreis', 6437: 'LK Odenwaldkreis', 6438: 'LK Offenbach', 6439: 'LK Rheingau-Taunus-Kreis', 6440: 'LK Wetteraukreis', 6531: 'LK Gießen', 6532: 'LK Lahn-Dill-Kreis', 6533: 'LK Limburg-Weilburg', 6534: 'LK Marburg-Biedenkopf', 6535: 'LK Vogelsbergkreis', 6611: 'SK Kassel', 6631: 'LK Fulda', 6632: 'LK Hersfeld-Rotenburg', 6633: 'LK Kassel', 6634: 'LK Schwalm-Eder-Kreis', 6635: 'LK Waldeck-Frankenberg', 6636: 'LK Werra-Meißner-Kreis', 7111: 'SK Koblenz', 7131: 'LK Ahrweiler', 7132: 'LK Altenkirchen', 7133: 'LK Bad Kreuznach', 7134: 'LK Birkenfeld', 7135: 'LK Cochem-Zell', 7137: 'LK Mayen-Koblenz', 7138: 'LK Neuwied', 7140: 'LK Rhein-Hunsrück-Kreis', 7141: 'LK Rhein-Lahn-Kreis', 7143: 'LK Westerwaldkreis', 7211: 'SK Trier', 7231: 'LK Bernkastel-Wittlich', 7232: 'LK Bitburg-Prüm', 7233: 'LK Vulkaneifel', 7235: 'LK Trier-Saarburg', 7311: 'SK Frankenthal', 7312: 'SK Kaiserslautern', 7313: 'SK Landau i.d.Pfalz', 7314: 'SK Ludwigshafen', 7315: 'SK Mainz', 7316: 'SK Neustadt a.d.Weinstraße', 7317: 'SK Pirmasens', 7318: 'SK Speyer', 7319: 'SK Worms', 7320: 'SK Zweibrücken', 7331: 'LK Alzey-Worms', 7332: 'LK Bad Dürkheim', 7333: 'LK Donnersbergkreis', 7334: 'LK Germersheim', 7335: 'LK Kaiserslautern', 7336: 'LK Kusel', 7337: 'LK Südliche Weinstraße', 7338: 'LK Rhein-Pfalz-Kreis', 7339: 'LK Mainz-Bingen', 7340: 'LK Südwestpfalz', 8111: 'SK Stuttgart', 8115: 'LK Böblingen', 8116: 'LK Esslingen', 8117: 'LK Göppingen', 8118: 'LK Ludwigsburg', 8119: 'LK Rems-Murr-Kreis', 8121: 'SK Heilbronn', 8125: 'LK Heilbronn', 8126: 'LK Hohenlohekreis', 8127: 'LK Schwäbisch Hall', 8128: 'LK Main-Tauber-Kreis', 8135: 'LK Heidenheim', 8136: 'LK Ostalbkreis', 8211: 'SK Baden-Baden', 8212: 'SK Karlsruhe', 8215: 'LK Karlsruhe', 8216: 'LK Rastatt', 8221: 'SK Heidelberg', 8222: 'SK Mannheim', 8225: 'LK Neckar-Odenwald-Kreis', 8226: 'LK Rhein-Neckar-Kreis', 8231: 'SK Pforzheim', 8235: 'LK Calw', 8236: 'LK Enzkreis', 8237: 'LK Freudenstadt', 8311: 'SK Freiburg i.Breisgau', 8315: 'LK Breisgau-Hochschwarzwald', 8316: 'LK Emmendingen', 8317: 'LK Ortenaukreis', 8325: 'LK Rottweil', 8326: 'LK Schwarzwald-Baar-Kreis', 8327: 'LK Tuttlingen', 8335: 'LK Konstanz', 8336: 'LK Lörrach', 8337: 'LK Waldshut', 8415: 'LK Reutlingen', 8416: 'LK Tübingen', 8417: 'LK Zollernalbkreis', 8421: 'SK Ulm', 8425: 'LK Alb-Donau-Kreis', 8426: 'LK Biberach', 8435: 'LK Bodenseekreis', 8436: 'LK Ravensburg', 8437: 'LK Sigmaringen', 9161: 'SK Ingolstadt', 9162: 'SK München', 9163: 'SK Rosenheim', 9171: 'LK Altötting', 9172: 'LK Berchtesgadener Land', 9173: 'LK Bad Tölz-Wolfratshausen', 9174: 'LK Dachau', 9175: 'LK Ebersberg', 9176: 'LK Eichstätt', 9177: 'LK Erding', 9178: 'LK Freising', 9179: 'LK Fürstenfeldbruck', 9180: 'LK Garmisch-Partenkirchen', 9181: 'LK Landsberg a.Lech', 9182: 'LK Miesbach', 9183: 'LK Mühldorf a.Inn', 9184: 'LK München', 9185: 'LK Neuburg-Schrobenhausen', 9186: 'LK Pfaffenhofen a.d.Ilm', 9187: 'LK Rosenheim', 9188: 'LK Starnberg', 9189: 'LK Traunstein', 9190: 'LK Weilheim-Schongau', 9261: 'SK Landshut', 9262: 'SK Passau', 9263: 'SK Straubing', 9271: 'LK Deggendorf', 9272: 'LK Freyung-Grafenau', 9273: 'LK Kelheim', 9274: 'LK Landshut', 9275: 'LK Passau', 9276: 'LK Regen', 9277: 'LK Rottal-Inn', 9278: 'LK Straubing-Bogen', 9279: 'LK Dingolfing-Landau', 9361: 'SK Amberg', 9362: 'SK Regensburg', 9363: 'SK Weiden i.d.OPf.', 9371: 'LK Amberg-Sulzbach', 9372: 'LK Cham', 9373: 'LK Neumarkt i.d.OPf.', 9374: 'LK Neustadt a.d.Waldnaab', 9375: 'LK Regensburg', 9376: 'LK Schwandorf', 9377: 'LK Tirschenreuth', 9461: 'SK Bamberg', 9462: 'SK Bayreuth', 9463: 'SK Coburg', 9464: 'SK Hof', 9471: 'LK Bamberg', 9472: 'LK Bayreuth', 9473: 'LK Coburg', 9474: 'LK Forchheim', 9475: 'LK Hof', 9476: 'LK Kronach', 9477: 'LK Kulmbach', 9478: 'LK Lichtenfels', 9479: 'LK Wunsiedel i.Fichtelgebirge', 9561: 'SK Ansbach', 9562: 'SK Erlangen', 9563: 'SK Fürth', 9564: 'SK Nürnberg', 9565: 'SK Schwabach', 9571: 'LK Ansbach', 9572: 'LK Erlangen-Höchstadt', 9573: 'LK Fürth', 9574: 'LK Nürnberger Land', 9575: 'LK Neustadt a.d.Aisch-Bad Windsheim', 9576: 'LK Roth', 9577: 'LK Weißenburg-Gunzenhausen', 9661: 'SK Aschaffenburg', 9662: 'SK Schweinfurt', 9663: 'SK Würzburg', 9671: 'LK Aschaffenburg', 9672: 'LK Bad Kissingen', 9673: 'LK Rhön-Grabfeld', 9674: 'LK Haßberge', 9675: 'LK Kitzingen', 9676: 'LK Miltenberg', 9677: 'LK Main-Spessart', 9678: 'LK Schweinfurt', 9679: 'LK Würzburg', 9761: 'SK Augsburg', 9762: 'SK Kaufbeuren', 9763: 'SK Kempten', 9764: 'SK Memmingen', 9771: 'LK Aichach-Friedberg', 9772: 'LK Augsburg', 9773: 'LK Dillingen a.d.Donau', 9774: 'LK Günzburg', 9775: 'LK Neu-Ulm', 9776: 'LK Lindau', 9777: 'LK Ostallgäu', 9778: 'LK Unterallgäu', 9779: 'LK Donau-Ries', 9780: 'LK Oberallgäu', 10041: 'LK Stadtverband Saarbrücken', 10042: 'LK Merzig-Wadern', 10043: 'LK Neunkirchen', 10044: 'LK Saarlouis', 10045: 'LK Saar-Pfalz-Kreis', 10046: 'LK Sankt Wendel', 11001: 'SK Berlin Mitte', 11002: 'SK Berlin Friedrichshain-Kreuzberg', 11003: 'SK Berlin Pankow', 11004: 'SK Berlin Charlottenburg-Wilmersdorf', 11005: 'SK Berlin Spandau', 11006: 'SK Berlin Steglitz-Zehlendorf', 11007: 'SK Berlin Tempelhof-Schöneberg', 11008: 'SK Berlin Neukölln', 11009: 'SK Berlin Treptow-Köpenick', 11010: 'SK Berlin Marzahn-Hellersdorf', 11011: 'SK Berlin Lichtenberg', 11012: 'SK Berlin Reinickendorf', 12051: 'SK Brandenburg a.d.Havel', 12052: 'SK Cottbus', 12053: 'SK Frankfurt (Oder)', 12054: 'SK Potsdam', 12060: 'LK Barnim', 12061: 'LK Dahme-Spreewald', 12062: 'LK Elbe-Elster', 12063: 'LK Havelland', 12064: 'LK Märkisch-Oderland', 12065: 'LK Oberhavel', 12066: 'LK Oberspreewald-Lausitz', 12067: 'LK Oder-Spree', 12068: 'LK Ostprignitz-Ruppin', 12069: 'LK Potsdam-Mittelmark', 12070: 'LK Prignitz', 12071: 'LK Spree-Neiße', 12072: 'LK Teltow-Fläming', 12073: 'LK Uckermark', 13003: 'SK Rostock', 13004: 'SK Schwerin', 13071: 'LK Mecklenburgische Seenplatte', 13072: 'LK Rostock', 13073: 'LK Vorpommern-Rügen', 13074: 'LK Nordwestmecklenburg', 13075: 'LK Vorpommern-Greifswald', 13076: 'LK Ludwigslust-Parchim', 14511: 'SK Chemnitz', 14521: 'LK Erzgebirgskreis', 14522: 'LK Mittelsachsen', 14523: 'LK Vogtlandkreis', 14524: 'LK Zwickau', 14612: 'SK Dresden', 14625: 'LK Bautzen', 14626: 'LK Görlitz', 14627: 'LK Meißen', 14628: 'LK Sächsische Schweiz-Osterzgebirge', 14713: 'SK Leipzig', 14729: 'LK Leipzig', 14730: 'LK Nordsachsen', 15001: 'SK Dessau-Roßlau', 15002: 'SK Halle', 15003: 'SK Magdeburg', 15081: 'LK Altmarkkreis Salzwedel', 15082: 'LK Anhalt-Bitterfeld', 15083: 'LK Börde', 15084: 'LK Burgenlandkreis', 15085: 'LK Harz', 15086: 'LK Jerichower Land', 15087: 'LK Mansfeld-Südharz', 15088: 'LK Saalekreis', 15089: 'LK Salzlandkreis', 15090: 'LK Stendal', 15091: 'LK Wittenberg', 16051: 'SK Erfurt', 16052: 'SK Gera', 16053: 'SK Jena', 16054: 'SK Suhl', 16055: 'SK Weimar', 16056: 'SK Eisenach', 16061: 'LK Eichsfeld', 16062: 'LK Nordhausen', 16063: 'LK Wartburgkreis', 16064: 'LK Unstrut-Hainich-Kreis', 16065: 'LK Kyffhäuserkreis', 16066: 'LK Schmalkalden-Meiningen', 16067: 'LK Gotha', 16068: 'LK Sömmerda', 16069: 'LK Hildburghausen', 16070: 'LK Ilm-Kreis', 16071: 'LK Weimarer Land', 16072: 'LK Sonneberg', 16073: 'LK Saalfeld-Rudolstadt', 16074: 'LK Saale-Holzland-Kreis', 16075: 'LK Saale-Orla-Kreis', 16076: 'LK Greiz', 16077: 'LK Altenburger Land'}
        # Delete Berlin
     #   del lkrN[11000]
        
     #   self.lkrN = lkrN
        
    def Print(self):
        
        for k,name in self.lkrNames.items():
            print(k,"'%s'"%name,self.lkrCodes[k],"\tN=%d"%self.lkrN[k])
        
    def GetLandkreisIDs(self):
        """ list of all LandkreisIDs """
        return self.lkrNames.keys()
    
    def GetSurvStatRKI_Suffix(self,lkrID):
        """ Returns the suffix neede for a SurvStat@RKI_2.0 query
            example (Hannover): .&[03].&[DE92].&[03241] """
        code = self.lkrCodes[lkrID]
        bundeslandID = lkrID//1000
        return ".&[%02d].&[%s].&[%05d]"%(bundeslandID,code,lkrID)
    

"""
# Landkreis adjacency
lkadj = {} 
lkadj[1001] = [1059,"DK"] # SK Flensbug
lkadj[1002] = [1057,1058] # Kiel
lkadj[1003] = [1053,1055,1062,13074] # Lübeck
lkadj[1004] = [1057,1058,1060] # Neumünster
lkadj[1051] = [1054,1059,1057,1061,3359,3352] # Dithmarschen
lkadj[1053] = [1003,1062,2000,3353,3355,13074,13076] # Herzogtum Lauenburg
lkadj[1054] = [1051,1059,"DK"] # Nordfriesland
lkadj[1055] = [1053,1058,1060,1062] # Ostholstein
lkadj[1056] = [1060,1061,2000,3359] # Pinneberg
lkadj[1057] = [1051,1058,1059,1060,1061,1002,1004] # Rendsburg-Eckernförde
lkadj[1058] = [1002,1004,1055,1057,1060] # Plön
lkadj[1059] = [1001,1051,1054,1057,"DK"] # Schleswig-Flensburg
lkadj[1060] = [1004,1055,1056,1057,1058,1061,1062,2000] # Segeberg
lkadj[1061] = [1051,1056,1057,1060,3359] # Steinburg
lkadj[1062] = [1003,1053,1055,1060,2000] # Stormarn
lkadj[2000] = [1053,1056,1060,1062,3353,3359] # Hamburg

lkadj[3352] = [3359] # Cuxhaven
lkadj[3353] = [2000,3355] # Harburg
lkadj[3355] = [1053,3353,3359,13076] # Lüneburg

lkadj[3359] = [1056,1061,2000,3352,3355] # Stade


lkadj[3101] = [] # SK Braunschweig
lkadj[3102] = [] # SK Salzgitter
lkadj[3103] = [] # SK Wolfsburg
lkadj[3151] = [] # LK Gifhorn
lkadj[3153] = [] # LK Goslar
lkadj[3154] = [] # LK Helmstedt
lkadj[3155] = [] # LK Northeim
lkadj[3157] = [] # LK Peine
lkadj[3158] = [] # LK Wolfenbüttel
lkadj[3159] = [] # LK Göttingen
lkadj[3241] = [] # Region Hannover
lkadj[3251] = [] # LK Diepholz
lkadj[3252] = [] # LK Hameln-Pyrmont
lkadj[3254] = [] # LK Hildesheim
lkadj[3255] = [] # LK Holzminden
lkadj[3256] = [] # LK Nienburg (Weser)
lkadj[3257] = [] # LK Schaumburg
lkadj[3351] = [] # LK Celle
lkadj[3352] = [] # LK Cuxhaven
lkadj[3353] = [] # LK Harburg
lkadj[3354] = [] # LK Lüchow-Dannenberg
lkadj[3355] = [] # LK Lüneburg
lkadj[3356] = [] # LK Osterholz
lkadj[3357] = [] # LK Rotenburg (Wümme)
lkadj[3358] = [] # LK Heidekreis
lkadj[3359] = [] # LK Stade
lkadj[3360] = [] # LK Uelzen
lkadj[3361] = [] # LK Verden
lkadj[3401] = [] # SK Delmenhorst
lkadj[3402] = [] # SK Emden
lkadj[3403] = [] # SK Oldenburg
lkadj[3404] = [] # SK Osnabrück
lkadj[3405] = [] # SK Wilhelmshaven
lkadj[3451] = [] # LK Ammerland
lkadj[3452] = [] # LK Aurich
lkadj[3453] = [] # LK Cloppenburg
lkadj[3454] = [] # LK Emsland
lkadj[3455] = [] # LK Friesland
lkadj[3456] = [] # LK Grafschaft Bentheim
lkadj[3457] = [] # LK Leer
lkadj[3458] = [] # LK Oldenburg
lkadj[3459] = [] # LK Osnabrück
lkadj[3460] = [] # LK Vechta
lkadj[3461] = [] # LK Wesermarsch
lkadj[3462] = [] # LK Wittmund
lkadj[4011] = [] # SK Bremen
lkadj[4012] = [] # SK Bremerhaven
lkadj[5111] = [] # SK Düsseldorf
lkadj[5112] = [] # SK Duisburg
lkadj[5113] = [] # SK Essen
lkadj[5114] = [] # SK Krefeld
lkadj[5116] = [] # SK Mönchengladbach
lkadj[5117] = [] # SK Mülheim a.d.Ruhr
lkadj[5119] = [] # SK Oberhausen
lkadj[5120] = [] # SK Remscheid
lkadj[5122] = [] # SK Solingen
lkadj[5124] = [] # SK Wuppertal
lkadj[5154] = [] # LK Kleve
lkadj[5158] = [] # LK Mettmann
lkadj[5162] = [] # LK Rhein-Kreis Neuss
lkadj[5166] = [] # LK Viersen
lkadj[5170] = [] # LK Wesel
lkadj[5314] = [] # SK Bonn
lkadj[5315] = [] # SK Köln
lkadj[5316] = [] # SK Leverkusen
lkadj[5334] = [] # StadtRegion Aachen
lkadj[5358] = [] # LK Düren
lkadj[5362] = [] # LK Rhein-Erft-Kreis
lkadj[5366] = [] # LK Euskirchen
lkadj[5370] = [] # LK Heinsberg
lkadj[5374] = [] # LK Oberbergischer Kreis
lkadj[5378] = [] # LK Rheinisch-Bergischer Kreis
lkadj[5382] = [] # LK Rhein-Sieg-Kreis
lkadj[5512] = [] # SK Bottrop
lkadj[5513] = [] # SK Gelsenkirchen
lkadj[5515] = [] # SK Münster
lkadj[5554] = [] # LK Borken
lkadj[5558] = [] # LK Coesfeld
lkadj[5562] = [] # LK Recklinghausen
lkadj[5566] = [] # LK Steinfurt
lkadj[5570] = [] # LK Warendorf
lkadj[5711] = [] # SK Bielefeld
lkadj[5754] = [] # LK Gütersloh
lkadj[5758] = [] # LK Herford
lkadj[5762] = [] # LK Höxter
lkadj[5766] = [] # LK Lippe
lkadj[5770] = [] # LK Minden-Lübbecke
lkadj[5774] = [] # LK Paderborn
lkadj[5911] = [] # SK Bochum
lkadj[5913] = [] # SK Dortmund
lkadj[5914] = [] # SK Hagen
lkadj[5915] = [] # SK Hamm
lkadj[5916] = [] # SK Herne
lkadj[5954] = [] # LK Ennepe-Ruhr-Kreis
lkadj[5958] = [] # LK Hochsauerlandkreis
lkadj[5962] = [] # LK Märkischer Kreis
lkadj[5966] = [] # LK Olpe
lkadj[5970] = [] # LK Siegen-Wittgenstein
lkadj[5974] = [] # LK Soest
lkadj[5978] = [] # LK Unna

lkadj[6411] = [] # SK Darmstadt
lkadj[6412] = [] # SK Frankfurt am Main
lkadj[6413] = [] # SK Offenbach
lkadj[6414] = [] # SK Wiesbaden
lkadj[6431] = [] # LK Bergstraße
lkadj[6432] = [] # LK Darmstadt-Dieburg
lkadj[6433] = [] # LK Groß-Gerau
lkadj[6434] = [] # LK Hochtaunuskreis
lkadj[6435] = [] # LK Main-Kinzig-Kreis
lkadj[6436] = [] # LK Main-Taunus-Kreis
lkadj[6437] = [] # LK Odenwaldkreis
lkadj[6438] = [] # LK Offenbach
lkadj[6439] = [] # LK Rheingau-Taunus-Kreis
lkadj[6440] = [] # LK Wetteraukreis
lkadj[6531] = [] # LK Gießen
lkadj[6532] = [] # LK Lahn-Dill-Kreis
lkadj[6533] = [] # LK Limburg-Weilburg
lkadj[6534] = [] # LK Marburg-Biedenkopf
lkadj[6535] = [] # LK Vogelsbergkreis
lkadj[6611] = [] # SK Kassel
lkadj[6631] = [] # LK Fulda
lkadj[6632] = [] # LK Hersfeld-Rotenburg
lkadj[6633] = [] # LK Kassel
lkadj[6634] = [] # LK Schwalm-Eder-Kreis
lkadj[6635] = [] # LK Waldeck-Frankenberg
lkadj[6636] = [] # LK Werra-Meißner-Kreis
lkadj[7111] = [] # SK Koblenz
lkadj[7131] = [] # LK Ahrweiler
lkadj[7132] = [] # LK Altenkirchen
lkadj[7133] = [] # LK Bad Kreuznach
lkadj[7134] = [] # LK Birkenfeld
lkadj[7135] = [] # LK Cochem-Zell
lkadj[7137] = [] # LK Mayen-Koblenz
lkadj[7138] = [] # LK Neuwied
lkadj[7140] = [] # LK Rhein-Hunsrück-Kreis
lkadj[7141] = [] # LK Rhein-Lahn-Kreis
lkadj[7143] = [] # LK Westerwaldkreis
lkadj[7211] = [] # SK Trier
lkadj[7231] = [] # LK Bernkastel-Wittlich
lkadj[7232] = [] # LK Bitburg-Prüm
lkadj[7233] = [] # LK Vulkaneifel
lkadj[7235] = [] # LK Trier-Saarburg
lkadj[7311] = [] # SK Frankenthal
lkadj[7312] = [] # SK Kaiserslautern
lkadj[7313] = [] # SK Landau i.d.Pfalz
lkadj[7314] = [] # SK Ludwigshafen
lkadj[7315] = [] # SK Mainz
lkadj[7316] = [] # SK Neustadt a.d.Weinstraße
lkadj[7317] = [] SK Pirmasens
lkadj[7318] = [] SK Speyer
lkadj[7319] = [] SK Worms
lkadj[7320] = [] SK Zweibrücken
lkadj[7331] = [] LK Alzey-Worms
lkadj[7332] = [] LK Bad Dürkheim
lkadj[7333] = [] LK Donnersbergkreis
lkadj[7334] = [] LK Germersheim
lkadj[7335] = [] LK Kaiserslautern
lkadj[7336] = [] LK Kusel
lkadj[7337] = [] LK Südliche Weinstraße
lkadj[7338] = [] LK Rhein-Pfalz-Kreis
lkadj[7339] = [] LK Mainz-Bingen
lkadj[7340] = [] LK Südwestpfalz
		
[8111] = [] # SK Stuttgart
[8115] = [] # LK Böblingen
[8116] = [] # LK Esslingen
[8117] = [] # LK Göppingen
[8118] = [] # LK Ludwigsburg
[8119] = [] # LK Rems-Murr-Kreis
[8121] = [] # SK Heilbronn
[8125] = [] # LK Heilbronn
[8126] = [] # LK Hohenlohekreis
[8127] = [] # LK Schwäbisch Hall
[8128] = [] # LK Main-Tauber-Kreis
[8135] = [] # LK Heidenheim
[8136] = [] # LK Ostalbkreis
[8211] = [] # SK Baden-Baden
[8212] = [] # SK Karlsruhe
[8215] = [] # LK Karlsruhe
[8216] = [] # LK Rastatt
[8221] = [] # SK Heidelberg
[8222] = [] # SK Mannheim
[8225] = [] # LK Neckar-Odenwald-Kreis
[8226] = [] # LK Rhein-Neckar-Kreis
[8231] = [] # SK Pforzheim
[8235] = [] # LK Calw
[8236] = [] # LK Enzkreis
[8237] = [] # LK Freudenstadt
[8311] = [] # SK Freiburg i.Breisgau
[8315] = [] # LK Breisgau-Hochschwarzwald
[8316] = [] # LK Emmendingen
[8317] = [] # LK Ortenaukreis
[8325] = [] # LK Rottweil
[8326] = [] # LK Schwarzwald-Baar-Kreis
[8327] = [] # LK Tuttlingen
[8335] = [] # LK Konstanz
[8336] = [] # LK Lörrach
[8337] = [] # LK Waldshut
[8415] = [] # LK Reutlingen
[8416] = [] # LK Tübingen
[8417] = [] # LK Zollernalbkreis
[8421] = [] # SK Ulm
[8425] = [] # LK Alb-Donau-Kreis
[8426] = [] # LK Biberach
[8435] = [] # LK Bodenseekreis
[8436] = [] # LK Ravensburg
[8437] = [] # LK Sigmaringen

[9161] = [] # SK Ingolstadt
[9162] = [] # SK München
[9163] = [] # SK Rosenheim
[9171] = [] # LK Altötting
[9172] = [] # LK Berchtesgadener Land
[9173] = [] # LK Bad Tölz-Wolfratshausen
[9174] = [] # LK Dachau
[9175] = [] # LK Ebersberg
[9176] = [] # LK Eichstätt
[9177] = [] # LK Erding
[9178] = [] # LK Freising
[9179] = [] # LK Fürstenfeldbruck
[9180] = [] # LK Garmisch-Partenkirchen', 9181: 'LK Landsberg a.Lech', 9182: 'LK Miesbach', 9183: 'LK Mühldorf a.Inn', 9184: 'LK München', 9185: 'LK Neuburg-Schrobenhausen', 9186: 'LK Pfaffenhofen a.d.Ilm', 9187: 'LK Rosenheim', 9188: 'LK Starnberg', 9189: 'LK Traunstein', 9190: 'LK Weilheim-Schongau', 9261: 'SK Landshut', 9262: 'SK Passau', 9263: 'SK Straubing', 9271: 'LK Deggendorf', 9272: 'LK Freyung-Grafenau', 9273: 'LK Kelheim', 9274: 'LK Landshut', 9275: 'LK Passau', 9276: 'LK Regen', 9277: 'LK Rottal-Inn', 9278: 'LK Straubing-Bogen', 9279: 'LK Dingolfing-Landau', 9361: 'SK Amberg', 9362: 'SK Regensburg', 9363: 'SK Weiden i.d.OPf.', 9371: 'LK Amberg-Sulzbach', 9372: 'LK Cham', 9373: 'LK Neumarkt i.d.OPf.', 9374: 'LK Neustadt a.d.Waldnaab', 9375: 'LK Regensburg', 9376: 'LK Schwandorf', 9377: 'LK Tirschenreuth', 9461: 'SK Bamberg', 9462: 'SK Bayreuth', 9463: 'SK Coburg', 9464: 'SK Hof', 9471: 'LK Bamberg', 9472: 'LK Bayreuth', 9473: 'LK Coburg', 9474: 'LK Forchheim', 9475: 'LK Hof', 9476: 'LK Kronach', 9477: 'LK Kulmbach', 9478: 'LK Lichtenfels', 9479: 'LK Wunsiedel i.Fichtelgebirge', 9561: 'SK Ansbach', 9562: 'SK Erlangen', 9563: 'SK Fürth', 9564: 'SK Nürnberg', 9565: 'SK Schwabach', 9571: 'LK Ansbach', 9572: 'LK Erlangen-Höchstadt', 9573: 'LK Fürth', 9574: 'LK Nürnberger Land', 9575: 'LK Neustadt a.d.Aisch-Bad Windsheim', 9576: 'LK Roth', 9577: 'LK Weißenburg-Gunzenhausen', 9661: 'SK Aschaffenburg', 9662: 'SK Schweinfurt', 9663: 'SK Würzburg', 9671: 'LK Aschaffenburg', 9672: 'LK Bad Kissingen', 9673: 'LK Rhön-Grabfeld', 9674: 'LK Haßberge', 9675: 'LK Kitzingen', 9676: 'LK Miltenberg', 9677: 'LK Main-Spessart', 9678: 'LK Schweinfurt', 9679: 'LK Würzburg', 9761: 'SK Augsburg', 9762: 'SK Kaufbeuren', 9763: 'SK Kempten', 9764: 'SK Memmingen', 9771: 'LK Aichach-Friedberg', 9772: 'LK Augsburg', 9773: 'LK Dillingen a.d.Donau', 9774: 'LK Günzburg', 9775: 'LK Neu-Ulm', 9776: 'LK Lindau', 9777: 'LK Ostallgäu', 9778: 'LK Unterallgäu', 9779: 'LK Donau-Ries', 9780: 'LK Oberallgäu',



lkadj[13074] = [1003,13076] # Nordwestmecklenburg
lkadj[13076] = [1053,13074] # Ludwigslust-Parchim
"""


def main():
    lks = Landkreise()
    lks.Print()
    
    print(lks.GetSurvStatRKI_Suffix(3241))
    print(lks.GetSurvStatRKI_Suffix(16077))
    

if __name__=="__main__":
    main()
