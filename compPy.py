#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyparsing import pyparsing_common as ppc
from pyparsing import Word, alphas, alphanums, CaselessKeyword
from pyparsing import MatchFirst, Forward

#>>>>>>>>>>>>>>> BASICS DEFINITIONS>>>>>>>>>>>>>>>>>>

#Defining the reserved words informed on the description
PROGRAMA, CAR, INT, RETORNE = map(CaselessKeyword,
                            "programa car int retorne".split())
ESCREVA, NOVALINHA, SE, ENTAO = map(CaselessKeyword,
                            "escreva novalinha se entao".split())
SENAO, ENQUANTO, EXECUTE, LEIA, TERMINATOR = map(CaselessKeyword,
                            "senao enquanto execute leia ;".split())

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
        LEIA,
        TERMINATOR
    )
).setName("Reserved Words")

#Define the numbers
realNum = ppc.real().setName("Real Number")
intNum = ppc.signed_integer().setName("Integer Number")

#Define the identificator
identifier = Word(alphas, alphanums + "_$").setName("Identifier")

#Types Definition
Type = (
    INT |
    CAR
).setName("Type")

#<<<<<<<<<<<<<<< BASICS DEFINITIONS<<<<<<<<<<<<<<<<<<

#>>>>>>>>>>>>>>> EXPRESSIONS DECLARATIONS>>>>>>>>>>>>>>>>>>

#Assigning the recursive expressions
Command = Forward()
Expr = Forward()
AssignExpr = Forward()
CondExpr = Forward()
OrExpr = Forward()
AndExpr = Forward()
EqExpr = Forward()
UneqExpr = Forward()
AddExpr = Forward()
MultExpr = Forward()
ListExpr = Forward()

#<<<<<<<<<<<<<<< EXPRESSIONS DECLARATIONS<<<<<<<<<<<<<<<<<<

#>>>>>>>>>>>>>>> EXPRESSIONS DEFINITIONS>>>>>>>>>>>>>>>>>>

#Defining the Lvalue Expression
LValueExpr = (
    (identifier + Word("[") + Expr + Word("[")) |
    identifier
)

#Defining the List of expressions body
ListExpr <<= (
    AssignExpr |
    (ListExpr + Word(",") + AssignExpr) 
).setName("Expression List")

#Defining the Primary expression body
PrimExpr = (
    (identifier + Word("(") + ListExpr + Word(")")) |
    (identifier + Word("()")) |
    (identifier + Word("[") + Expr + Word("]")) |
    identifier |
    # carconst |
    # intconst |
    (Word("(") +  Expr + Word("("))
).setName("Primary Expression")

#Defining the Unary expression body
UnExpr = (
    (Word("-") + PrimExpr) |
    (Word("!") + PrimExpr) |
    PrimExpr
).setName("Unary Expression")

#Defining the MULT expression body
MultExpr <<= (
    (MultExpr + Word("*") + UnExpr) |
    (MultExpr + Word("/") + UnExpr) |
    (MultExpr + Word("%") + UnExpr) |
    UnExpr
).setName("MULT Expression")

#Defining the ADD expression body
AddExpr <<= (
    (AddExpr + Word("+") + MultExpr) |
    (AddExpr + Word("-") + MultExpr) |
    MultExpr
).setName("ADD Expression")

#Defining the Unequal expression body
UneqExpr <<= (
    (UneqExpr + Word("<") + AddExpr) |
    (UneqExpr + Word(">") + AddExpr) |
    (UneqExpr + Word(">=") + AddExpr) |
    (UneqExpr + Word("<=") + AddExpr) |
    AddExpr
).setName("Unequal Expression")

#Defining the Equal expression body
EqExpr <<= (
    (EqExpr + Word("==") + UneqExpr) |
    (EqExpr + Word("!=") + UneqExpr) |
    UneqExpr
).setName("Equal Expression")

#Defining the AND expression body
AndExpr <<= (
    (AndExpr + Word("e") + EqExpr) |
    EqExpr
).setName("AND Expression")

#Defining the OR expression body
OrExpr <<= (
    (OrExpr + Word("ou") + AndExpr) |
    AndExpr
).setName("OR Expression")

#Defining the conditional expression body
CondExpr <<= (
    OrExpr |
    (OrExpr + Word("?") + Expr + Word(":") + CondExpr)
).setName("Conditional Expression")

#defining the assigned expresion's body
AssignExpr <<= (
    CondExpr |
    (LValueExpr + Word("=") + AssignExpr) 
).setName("Assigned Expression")

#Defining the expression's body
Expr <<= AssignExpr.setName("Expression")

#Defining the command's body
Command <<= (
    TERMINATOR |
    (Expr + TERMINATOR) |
    (RETORNE + Expr + TERMINATOR) |
    (LEIA + LValueExpr + TERMINATOR) |
    (ESCREVA + Expr + TERMINATOR) |
    (ESCREVA + Word(alphanums) + TERMINATOR) |
    (NOVALINHA + TERMINATOR) |
    (SE + Word("(") + Expr + Word(")") + ENTAO + Command) |
    (SE + Word("(") + Expr + Word(")") + ENTAO + Command + SENAO + Command) |
    (ENQUANTO + Word("(") + Expr + Word(")") + EXECUTE + Command) 
    # | Block
).setName("Command")

#<<<<<<<<<<<<<<< EXPRESSIONS DEFINITIONS<<<<<<<<<<<<<<<<<<