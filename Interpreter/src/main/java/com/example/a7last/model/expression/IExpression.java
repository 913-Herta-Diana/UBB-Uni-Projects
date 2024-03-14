package com.example.a7last.model.expression;

import com.example.a7last.exceptions.InterpreterException;
import com.example.a7last.model.type.Type;
import com.example.a7last.model.utils.MyIDictionary;
import com.example.a7last.model.utils.MyIHeap;
import com.example.a7last.model.value.Value;

public interface IExpression {
    Type typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException;
    Value eval(MyIDictionary<String, Value> table, MyIHeap heap) throws InterpreterException;
    IExpression deepCopy();
}
