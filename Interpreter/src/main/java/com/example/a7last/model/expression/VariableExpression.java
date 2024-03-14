package com.example.a7last.model.expression;

import com.example.a7last.exceptions.InterpreterException;
import com.example.a7last.model.type.Type;
import com.example.a7last.model.utils.MyIDictionary;
import com.example.a7last.model.utils.MyIHeap;
import com.example.a7last.model.value.Value;

public class VariableExpression implements IExpression {
    String key;

    public VariableExpression(String key) {
        this.key = key;
    }

    @Override
    public Type typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        try {
            return typeEnv.lookUp(key);
        } catch (InterpreterException e) {
            e.printStackTrace();
        }
        return null;
    }

    @Override
    public Value eval(MyIDictionary<String, Value> table, MyIHeap heap) throws InterpreterException {
        try {
            return table.lookUp(key);
        } catch (InterpreterException e) {
            e.printStackTrace();
        }
        return null;
    }

    @Override
    public IExpression deepCopy() {
        return new VariableExpression(key);
    }

    @Override
    public String toString() {
        return key;
    }
}
