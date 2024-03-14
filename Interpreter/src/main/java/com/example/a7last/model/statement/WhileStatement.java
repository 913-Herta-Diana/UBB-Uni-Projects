package com.example.a7last.model.statement;

import com.example.a7last.exceptions.InterpreterException;
import com.example.a7last.model.expression.IExpression;
import com.example.a7last.model.programState.ProgramState;
import com.example.a7last.model.type.BoolType;
import com.example.a7last.model.type.Type;
import com.example.a7last.model.utils.MyIDictionary;
import com.example.a7last.model.utils.MyIStack;
import com.example.a7last.model.value.BoolValue;
import com.example.a7last.model.value.Value;

public class WhileStatement implements IStatement{
    private final IExpression expression;
    private final IStatement statement;

    public WhileStatement(IExpression expression, IStatement statement) {
        this.expression = expression;
        this.statement = statement;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        Value value = expression.eval(state.getSymTable(), state.getHeap());
        MyIStack<IStatement> stack = state.getExeStack();
        if (!value.getType().equals(new BoolType()))
            throw new InterpreterException(String.format("%s is not of BoolType", value));
        if (!(value instanceof BoolValue boolValue))
            throw new InterpreterException(String.format("%s is not a BoolValue", value));
        if (boolValue.getValue()) {
            stack.push(this.deepCopy());
            stack.push(statement);
        }
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        Type typeExpr = expression.typeCheck(typeEnv);
        if (typeExpr.equals(new BoolType())) {
            statement.typeCheck(typeEnv.deepCopy());
            return typeEnv;
        } else
            throw new InterpreterException("The condition of WHILE does not have the type Bool.");
    }

    @Override
    public IStatement deepCopy() {
        return new WhileStatement(expression.deepCopy(), statement.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("while(%s){%s}", expression, statement);
    }
}
