"""
Authors: Stefan Strang
University of Freiburg - 2018

"""

import doctest
from LTL.tests.unitTests import test
from LTL.tests.unitTest2 import test2
from LTL.tests.unitTestDef8ex2 import testgfp
from LTL.tests.testDef10 import test10
from LTL.tests.testDef10Ex import testEx
from LTL.tests.testDef10ExDoc import test10ex1
from LTL.tests.lfMiddleComplex import lfMedium
from LTL.tests.lfMedium2 import lfMedium2
from LTL.tests.lfMedium3 import lfMedium3
from LTL.tests.structureTest import structure
from LTL.tests.pdMedium1 import pdMedium
from LTL.tests.pdMedium2 import pdMedium2
from LTL.tests.testTableauDecision import testTableau
from LTL.tests.concatError import concatErr
from LTL.tests.testDef6 import def6
from LTL.tests.testOmegaAutomaton import testAuto


def testMain():
    doctest.testmod()

    # testing the strucutre
    doctest.testfile("../tools/getInp.py")
    doctest.testfile("../tools/ltlToPred.py")
    doctest.testfile("../tools/toPnfObjects.py")
    doctest.testfile("../tools/tableauDecision.py")
    structure()

    # testing linear factors
    doctest.testfile("../tools/lf.py")
    doctest.testfile("../tests/unitTestDef8ex2.py")
    # doctest.testfile("../tests/testDef10ExDoc.py")
    test()
    test2()
    testgfp()
    lfMedium()
    lfMedium2()
    lfMedium3()
    concatErr()

    # testing partial derivatives
    test10()
    testEx()
    test10ex1()
    pdMedium()
    pdMedium2()
    def6()
    pdMedium()

    # test omega automaton
    testAuto()
    testTableau()
    pdMedium2()
