package com.example.a7last.repository;

import com.example.a7last.exceptions.InterpreterException;
import  com.example.a7last.model.programState.ProgramState;

import java.io.IOException;
import java.util.List;

public interface IRepository {
    List<ProgramState> getProgramList();
    void setProgramStates(List<ProgramState> programStates);
    void addProgram(ProgramState program);
    void logPrgStateExec(ProgramState programState) throws IOException, InterpreterException;
    void emptyLogFile() throws IOException;
}
