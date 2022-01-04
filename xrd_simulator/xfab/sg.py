from __future__ import absolute_import
import xrd_simulator
from xrd_simulator.xfab import sglib
import numpy as n
from re import sub


class sg:
    def __init__(self, sgno = None, sgname = None, cell_choice = "standard"):
        if sgno != None:
            klass_name = "".join('Sg%i' %sgno)
        elif sgname != None:
            klass_name = sgdic[sub("\s+", "", sgname).lower()]
            if sub("\s+", "", sgname).lower()[0]=="r" and sub("\s+", "", sgname).lower()[-1]=="r":
                cell_choice = "rhombohedral"
        if hasattr(xrd_simulator.xfab, 'sglib'):
            module = getattr(xrd_simulator.xfab, 'sglib')
            if hasattr(module, klass_name):
                klass  = getattr(module, klass_name)
            else:
                raise Exception("No " + klass_name + " class in sglib")
        else:
            raise Exception("sglib module cannot be reached")

        obj = klass(cell_choice=cell_choice)

        self.name = obj.name
        self.no = obj.no
        self.crystal_system = obj.crystal_system
        self.nsymop = obj.nsymop
        self.nuniq = obj.nuniq
        self.Laue = obj.Laue
        self.syscond = n.array(obj.syscond)
        self.rot = n.array(obj.rot)
        self.trans = n.array(obj.trans)
        self.cell_choice = obj.cell_choice



sgdic = {
         "p1" : "Sg1",
         "p-1" : "Sg2",
         "p2" : "Sg3",
         "p21" : "Sg4",
         "c2" : "Sg5",
         "pm" : "Sg6",
         "pc" : "Sg7",
         "cm" : "Sg8",
         "cc" : "Sg9",
         "p2/m" : "Sg10",
         "p21/m" : "Sg11",
         "c2/m" : "Sg12",
         "p2/c" : "Sg13",
         "p21/c" : "Sg14",
         "c2/c" : "Sg15",
         "p222" : "Sg16",
         "p2221" : "Sg17",
         "p21212" : "Sg18",
         "p212121" : "Sg19",
         "c2221" : "Sg20",
         "c222" : "Sg21",
         "f222" : "Sg22",
         "i222" : "Sg23",
         "i212121" : "Sg24",
         "pmm2" : "Sg25",
         "pmc21" : "Sg26",
         "pcc2" : "Sg27",
         "pma2" : "Sg28",
         "pca21" : "Sg29",
         "pnc2" : "Sg30",
         "pmn21" : "Sg31",
         "pba2" : "Sg32",
         "pna21" : "Sg33",
         "pnn2" : "Sg34",
         "cmm2" : "Sg35",
         "cmc21" : "Sg36",
         "ccc2" : "Sg37",
         "amm2" : "Sg38",
         "abm2" : "Sg39",
         "ama2" : "Sg40",
         "aba2" : "Sg41",
         "fmm2" : "Sg42",
         "fdd2" : "Sg43",
         "imm2" : "Sg44",
         "iba2" : "Sg45",
         "ima2" : "Sg46",
         "pmmm" : "Sg47",
         "pnnn" : "Sg48",
         "pccm" : "Sg49",
         "pban" : "Sg50",
         "pmma" : "Sg51",
         "pnna" : "Sg52",
         "pmna" : "Sg53",
         "pcca" : "Sg54",
         "pbam" : "Sg55",
         "pccn" : "Sg56",
         "pbcm" : "Sg57",
         "pnnm" : "Sg58",
         "pmmn" : "Sg59",
         "pbcn" : "Sg60",
         "pbca" : "Sg61",
         "pnma" : "Sg62",
         "cmcm" : "Sg63",
         "cmca" : "Sg64",
         "cmmm" : "Sg65",
         "cccm" : "Sg66",
         "cmma" : "Sg67",
         "ccca" : "Sg68",
         "fmmm" : "Sg69",
         "fddd" : "Sg70",
         "immm" : "Sg71",
         "ibam" : "Sg72",
         "ibca" : "Sg73",
         "imma" : "Sg74",
         "p4" : "Sg75",
         "p41" : "Sg76",
         "p42" : "Sg77",
         "p43" : "Sg78",
         "i4" : "Sg79",
         "i41" : "Sg80",
         "p-4" : "Sg81",
         "i-4" : "Sg82",
         "p4/m" : "Sg83",
         "p42/m" : "Sg84",
         "p4/n" : "Sg85",
         "p42/n" : "Sg86",
         "i4/m" : "Sg87",
         "i41/a" : "Sg88",
         "p422" : "Sg89",
         "p4212" : "Sg90",
         "p4122" : "Sg91",
         "p41212" : "Sg92",
         "p4222" : "Sg93",
         "p42212" : "Sg94",
         "p4322" : "Sg95",
         "p43212" : "Sg96",
         "i422" : "Sg97",
         "i4122" : "Sg98",
         "p4mm" : "Sg99",
         "p4bm" : "Sg100",
         "p42cm" : "Sg101",
         "p42nm" : "Sg102",
         "p4cc" : "Sg103",
         "p4nc" : "Sg104",
         "p42mc" : "Sg105",
         "p42bc" : "Sg106",
         "i4mm" : "Sg107",
         "i4cm" : "Sg108",
         "i41md" : "Sg109",
         "i41cd" : "Sg110",
         "p-42m" : "Sg111",
         "p-42c" : "Sg112",
         "p-421m" : "Sg113",
         "p-421c" : "Sg114",
         "p-4m2" : "Sg115",
         "p-4c2" : "Sg116",
         "p-4b2" : "Sg117",
         "p-4n2" : "Sg118",
         "i-4m2" : "Sg119",
         "i-4c2" : "Sg120",
         "i-42m" : "Sg121",
         "i-42d" : "Sg122",
         "p4/mmm" : "Sg123",
         "p4/mcc" : "Sg124",
         "p4/nbm" : "Sg125",
         "p4/nnc" : "Sg126",
         "p4/mbm" : "Sg127",
         "p4/mnc" : "Sg128",
         "p4/nmm" : "Sg129",
         "p4/ncc" : "Sg130",
         "p42/mmc" : "Sg131",
         "p42/mcm" : "Sg132",
         "p42/nbc" : "Sg133",
         "p42/nnm" : "Sg134",
         "p42/mbc" : "Sg135",
         "p42/mnm" : "Sg136",
         "p42/nmc" : "Sg137",
         "p42/ncm" : "Sg138",
         "i4/mmm" : "Sg139",
         "i4/mcm" : "Sg140",
         "i41/amd" : "Sg141",
         "i41/acd" : "Sg142",
         "p3" : "Sg143",
         "p31" : "Sg144",
         "p32" : "Sg145",
         "r3" : "Sg146",
         "r3h" : "Sg146",
         "r3r" : "Sg146",
         "p-3" : "Sg147",
         "r-3" : "Sg148",
         "r-3h" : "Sg148",
         "r-3r" : "Sg148",
         "p312" : "Sg149",
         "p321" : "Sg150",
         "p3112" : "Sg151",
         "p3121" : "Sg152",
         "p3212" : "Sg153",
         "p3221" : "Sg154",
         "r32" : "Sg155",
         "r32h" : "Sg155",
         "r32r" : "Sg155",
         "p3m1" : "Sg156",
         "p31m" : "Sg157",
         "p3c1" : "Sg158",
         "p31c" : "Sg159",
         "r3m" : "Sg160",
         "r3mh" : "Sg160",
         "r3mr" : "Sg160",
         "r3c" : "Sg161",
         "r3ch" : "Sg161",
         "r3cr" : "Sg161",
         "p-31m" : "Sg162",
         "p-31c" : "Sg163",
         "p-3m1" : "Sg164",
         "p-3c1" : "Sg165",
         "r-3m" : "Sg166",
         "r-3mh" : "Sg166",
         "r-3mr" : "Sg166",
         "r-3c" : "Sg167",
         "r-3ch" : "Sg167",
         "r-3cr" : "Sg167",
         "p6" : "Sg168",
         "p61" : "Sg169",
         "p65" : "Sg170",
         "p62" : "Sg171",
         "p64" : "Sg172",
         "p63" : "Sg173",
         "p-6" : "Sg174",
         "p6/m" : "Sg175",
         "p63/m" : "Sg176",
         "p622" : "Sg177",
         "p6122" : "Sg178",
         "p6522" : "Sg179",
         "p6222" : "Sg180",
         "p6422" : "Sg181",
         "p6322" : "Sg182",
         "p6mm" : "Sg183",
         "p6cc" : "Sg184",
         "p63cm" : "Sg185",
         "p63mc" : "Sg186",
         "p-6m2" : "Sg187",
         "p-6c2" : "Sg188",
         "p-62m" : "Sg189",
         "p-62c" : "Sg190",
         "p6/mmm" : "Sg191",
         "p6/mcc" : "Sg192",
         "p63/mcm" : "Sg193",
         "p63/mmc" : "Sg194",
         "p23" : "Sg195",
         "f23" : "Sg196",
         "i23" : "Sg197",
         "p213" : "Sg198",
         "i213" : "Sg199",
         "pm-3" : "Sg200",
         "pn-3" : "Sg201",
         "fm-3" : "Sg202",
         "fd-3" : "Sg203",
         "im-3" : "Sg204",
         "pa-3" : "Sg205",
         "ia-3" : "Sg206",
         "p432" : "Sg207",
         "p4232" : "Sg208",
         "f432" : "Sg209",
         "f4132" : "Sg210",
         "i432" : "Sg211",
         "p4332" : "Sg212",
         "p4132" : "Sg213",
         "i4132" : "Sg214",
         "p-43m" : "Sg215",
         "f-43m" : "Sg216",
         "i-43m" : "Sg217",
         "p-43n" : "Sg218",
         "f-43c" : "Sg219",
         "i-43d" : "Sg220",
         "pm-3m" : "Sg221",
         "pn-3n" : "Sg222",
         "pm-3n" : "Sg223",
         "pn-3m" : "Sg224",
         "fm-3m" : "Sg225",
         "fm-3c" : "Sg226",
         "fd-3m" : "Sg227",
         "fd-3c" : "Sg228",
         "im-3m" : "Sg229",
         "ia-3d" : "Sg230",
        }