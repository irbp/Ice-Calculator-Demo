# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.7.0
#
# <auto-generated>
#
# Generated from file `Calculadora.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module Demo
_M_Demo = Ice.openModule('Demo')
__name__ = 'Demo'

_M_Demo._t_Calculator = IcePy.defineValue('::Demo::Calculator', Ice.Value, -1, (), False, True, None, ())

if 'CalculatorPrx' not in _M_Demo.__dict__:
    _M_Demo.CalculatorPrx = Ice.createTempClass()
    class CalculatorPrx(Ice.ObjectPrx):

        def add(self, a, b, context=None):
            return _M_Demo.Calculator._op_add.invoke(self, ((a, b), context))

        def addAsync(self, a, b, context=None):
            return _M_Demo.Calculator._op_add.invokeAsync(self, ((a, b), context))

        def begin_add(self, a, b, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Calculator._op_add.begin(self, ((a, b), _response, _ex, _sent, context))

        def end_add(self, _r):
            return _M_Demo.Calculator._op_add.end(self, _r)

        def sub(self, a, b, context=None):
            return _M_Demo.Calculator._op_sub.invoke(self, ((a, b), context))

        def subAsync(self, a, b, context=None):
            return _M_Demo.Calculator._op_sub.invokeAsync(self, ((a, b), context))

        def begin_sub(self, a, b, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Calculator._op_sub.begin(self, ((a, b), _response, _ex, _sent, context))

        def end_sub(self, _r):
            return _M_Demo.Calculator._op_sub.end(self, _r)

        def mul(self, a, b, context=None):
            return _M_Demo.Calculator._op_mul.invoke(self, ((a, b), context))

        def mulAsync(self, a, b, context=None):
            return _M_Demo.Calculator._op_mul.invokeAsync(self, ((a, b), context))

        def begin_mul(self, a, b, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Calculator._op_mul.begin(self, ((a, b), _response, _ex, _sent, context))

        def end_mul(self, _r):
            return _M_Demo.Calculator._op_mul.end(self, _r)

        def div(self, a, b, context=None):
            return _M_Demo.Calculator._op_div.invoke(self, ((a, b), context))

        def divAsync(self, a, b, context=None):
            return _M_Demo.Calculator._op_div.invokeAsync(self, ((a, b), context))

        def begin_div(self, a, b, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Calculator._op_div.begin(self, ((a, b), _response, _ex, _sent, context))

        def end_div(self, _r):
            return _M_Demo.Calculator._op_div.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Demo.CalculatorPrx.ice_checkedCast(proxy, '::Demo::Calculator', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Demo.CalculatorPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Demo::Calculator'
    _M_Demo._t_CalculatorPrx = IcePy.defineProxy('::Demo::Calculator', CalculatorPrx)

    _M_Demo.CalculatorPrx = CalculatorPrx
    del CalculatorPrx

    _M_Demo.Calculator = Ice.createTempClass()
    class Calculator(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Demo::Calculator', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Demo::Calculator'

        @staticmethod
        def ice_staticId():
            return '::Demo::Calculator'

        def add(self, a, b, current=None):
            raise NotImplementedError("servant method 'add' not implemented")

        def sub(self, a, b, current=None):
            raise NotImplementedError("servant method 'sub' not implemented")

        def mul(self, a, b, current=None):
            raise NotImplementedError("servant method 'mul' not implemented")

        def div(self, a, b, current=None):
            raise NotImplementedError("servant method 'div' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Demo._t_CalculatorDisp)

        __repr__ = __str__

    _M_Demo._t_CalculatorDisp = IcePy.defineClass('::Demo::Calculator', Calculator, (), None, ())
    Calculator._ice_type = _M_Demo._t_CalculatorDisp

    Calculator._op_add = IcePy.Operation('add', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_double, False, 0), ((), IcePy._t_double, False, 0)), (), ((), IcePy._t_double, False, 0), ())
    Calculator._op_sub = IcePy.Operation('sub', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_double, False, 0), ((), IcePy._t_double, False, 0)), (), ((), IcePy._t_double, False, 0), ())
    Calculator._op_mul = IcePy.Operation('mul', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_double, False, 0), ((), IcePy._t_double, False, 0)), (), ((), IcePy._t_double, False, 0), ())
    Calculator._op_div = IcePy.Operation('div', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_double, False, 0), ((), IcePy._t_double, False, 0)), (), ((), IcePy._t_double, False, 0), ())

    _M_Demo.Calculator = Calculator
    del Calculator

# End of module Demo
