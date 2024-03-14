package com.example.a7last.model.statement;

import com.example.a7last.exceptions.InterpreterException;
import com.example.a7last.model.expression.IExpression;
import com.example.a7last.model.programState.ProgramState;
import com.example.a7last.model.type.BoolType;
import com.example.a7last.model.type.Type;
import com.example.a7last.model.utils.MyIDictionary;

public class DoWhileStatement implements IStatement{
    private final IStatement statement;
    private final IExpression expression;

    public DoWhileStatement(IExpression expression, IStatement statement) {
        this.statement = statement;
        this.expression = expression;
    }
    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        IStatement converted = new CompoundStatement(statement, new WhileStatement(expression, statement));
        state.getExeStack().push(converted);
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        Type typeExpression = expression.typeCheck(typeEnv);
        if (typeExpression.equals(new BoolType())) {
            statement.typeCheck(typeEnv.deepCopy());
            return typeEnv;
        } else
            throw new InterpreterException("Condition in the do while statement must be bool!");
    }

    @Override
    public IStatement deepCopy() {
        return new DoWhileStatement(expression.deepCopy(), statement.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("do {%s} while (%s)", statement, expression);
    }
}