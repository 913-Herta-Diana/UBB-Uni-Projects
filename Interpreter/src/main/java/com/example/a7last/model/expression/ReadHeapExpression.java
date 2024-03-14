package com.example.a7last.model.expression;

import com.example.a7last.exceptions.InterpreterException;
import com.example.a7last.model.type.RefType;
import com.example.a7last.model.type.Type;
import com.example.a7last.model.utils.MyIDictionary;
import com.example.a7last.model.utils.MyIHeap;
import com.example.a7last.model.value.RefValue;
import com.example.a7last.model.value.Value;

public class ReadHeapExpression implements IExpression{
    private final IExpression expression;

    public ReadHeapExpression(IExpression expression) {
        this.expression = expression;
    }

    @Override
    public Type typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        Type type = expression.typeCheck(typeEnv);
        if (type instanceof RefType refType) {
            return refType.getInner();
        } else
            throw new InterpreterException("The rH argument is not a RefType.");
    }

    @Override
    public Value eval(MyIDictionary<String, Value> symTable, MyIHeap heap) throws InterpreterException {
        Value value = expression.eval(symTable, heap);
        if (value instanceof RefValue refValue) {
            if (heap.containsKey(refValue.getAddress()))
                try {
                    return heap.get(refValue.getAddress());
                } catch (InterpreterException e) {
                    e.printStackTrace();
                }
            else
                throw new InterpreterException("The address is not defined on the heap!");
        } else
            throw new InterpreterException(String.format("%s not of RefType", value));
        return null;
    }

    @Override
    public IExpression deepCopy() {
        return new ReadHeapExpression(expression.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("ReadHeap(%s)", expression);
    }
}
