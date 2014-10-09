import java.util.Map;
import java.util.TreeMap;

import java.io.IOException;
import java.util.*;
        
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
        
public class WordCount {
        
 public static class Map extends Mapper<LongWritable, Text, Text, IntWritable> {
    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();

    public void map(LongWritable key, Text value, Context context) 
                throws IOException, InterruptedException {
        
        String line = value.toString();
        StringTokenizer tokenizer = new StringTokenizer(line);
        while (tokenizer.hasMoreTokens()) {
            String nextWord = tokenizer.nextToken();
            if (nextWord.length() == 7) {
                word.set(nextWord);
                context.write(word, one);
            }
        }
    }
 } 
        
 public static class Reduce extends Reducer<Text, IntWritable, Text, IntWritable> {
    private TreeMap<Integer, ArrayList<String>> repToRecordMap = new TreeMap<Integer,ArrayList<String>>();
    private Text word = new Text();
    public void reduce(Text key, Iterable<IntWritable> values, Context context) 
      throws IOException, InterruptedException {
        int sum = 0;
        for (IntWritable val : values) {
            sum += val.get();
        }
        // context.write(key, new IntWritable(sum));
        String treeKey = key.toString();

        ArrayList<String> newStringList = new ArrayList<String>();
        if (!repToRecordMap.containsKey(sum)) {
        //     sum = sum + repToRecordMap.get(treeKey);
            newStringList.add(treeKey);
            }
        else {
            newStringList = repToRecordMap.get(sum);
            newStringList.add(treeKey);
        }
        repToRecordMap.put(sum , newStringList);

        
    }

    protected void cleanup(Context context) throws IOException, InterruptedException {
        int limit =100;
        int tmpKey;
        while (limit>0 && repToRecordMap.size()>0) {
            tmpKey = repToRecordMap.lastKey();
            ArrayList<String> values = repToRecordMap.get(tmpKey);
            for (int i= 0; i< values.size(); i++) {
                word.set(values.get(i));
                context.write(word, new IntWritable(tmpKey));
                limit--;
            }
            repToRecordMap.remove(tmpKey);
            
        }
    }
 }
        
 public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
        
        Job job = new Job(conf, "wordcount");
    
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
        
    job.setMapperClass(Map.class);
    job.setReducerClass(Reduce.class);
        
    job.setInputFormatClass(TextInputFormat.class);
    job.setOutputFormatClass(TextOutputFormat.class);

    job.setNumReduceTasks(1);
    job.setJarByClass(WordCount.class);
        
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
        
    job.waitForCompletion(true);
 }
        
}