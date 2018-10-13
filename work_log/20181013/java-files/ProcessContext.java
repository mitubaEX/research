//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

package net.sf.mmm.util.process.api;

import java.io.InputStream;
import java.io.OutputStream;
import net.sf.mmm.util.io.api.DevNullSource;
import net.sf.mmm.util.io.api.DevNullTarget;

public class ProcessContext {
    private OutputStream outStream;
    private OutputStream errStream;
    private InputStream inStream;
    private boolean keepStreamsOpen;

    public ProcessContext() {
        this.inStream = DevNullSource.INSTANCE;
        this.outStream = DevNullTarget.INSTANCE;
        this.errStream = DevNullTarget.INSTANCE;
    }

    public OutputStream getOutStream() {
        return this.outStream;
    }

    public void setOutStream(OutputStream outStream) {
        this.outStream = outStream;
    }

    public OutputStream getErrStream() {
        return this.errStream;
    }

    public void setErrStream(OutputStream errStream) {
        this.errStream = errStream;
    }

    public InputStream getInStream() {
        return this.inStream;
    }

    public void setInStream(InputStream inStream) {
        this.inStream = inStream;
    }

    public boolean isKeepStreamsOpen() {
        return this.keepStreamsOpen;
    }

    public void setKeepStreamsOpen(boolean keepStreamsOpen) {
        this.keepStreamsOpen = keepStreamsOpen;
    }
}

