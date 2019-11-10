#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyparsing import pyparsing_common as ppc
from pyparsing import Word, alphas, alphanums, CaselessKeyword
from pyparsing import MatchFirst

#Define the numbers
realNum = ppc.real()
intNum = ppc.signed_integer()

#Define the reserved words
PROGRAMA, CAR, INT, RETORNE = map(CaselessKeyword,
                            "programa car int retorne".split())
ESCREVA, NOVALINHA, SE, ENTAO = map(CaselessKeyword,
                            "escreva novalinha se entao".split())
SENAO, ENQUANTO, EXECUTE, LEIA = map(CaselessKeyword,
                            "senao enquanto execute leia".split())

keywords = MatchFirst(
    (
        PROGRAMA,
        CAR,
        INT,
        RETORNE,
        ESCREVA,
        NOVALINHA,
        SE,
        ENTAO,
        SENAO,
        ENQUANTO,
        EXECUTE,
        LEIA
    )
)