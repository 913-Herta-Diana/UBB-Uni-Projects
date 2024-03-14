package com.example.a7last.model.statement;

import com.example.a7last.exceptions.InterpreterException;
import com.example.a7last.model.expression.IExpression;
import com.example.a7last.model.programState.ProgramState;
import com.example.a7last.model.type.Type;
import com.example.a7last.model.utils.MyIDictionary;
import com.example.a7last.model.utils.MyIList;
import com.example.a7last.model.value.Value;

public class PrintStatement implements IStatement {
    IExpression expression;

    public PrintStatement(IExpression expression) {
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        MyIList<Value> out = state.getOut();
        out.add(expression.eval(state.getSymTable(), state.getHeap()));
        state.setOut(out);
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        expression.typeCheck(typeEnv);
        return typeEnv;
    }

    @Override
    public IStatement deepCopy() {
        return new PrintStatement(expression.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("Print(%s)", expression.toString());
    }
}
