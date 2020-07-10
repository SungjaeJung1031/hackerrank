package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
    "sort"
)

// Complete the organizingContainers function below.
func organizingContainers(container [][]int32) string {
    res := "Possible"
    var sliceCntType []int32
    var sliceCntContainer []int32

    for i := 0; i < len(container); i++{
        sliceCntType = append(sliceCntContainer, 0)
        sliceCntContainer = append(sliceCntContainer, 0)
    }
    
    for i, row := range container{
        for j, elem := range row{
            sliceCntType[j] += elem
            sliceCntContainer[i] += elem
        }
    }

    sort.Slice(sliceCntType, func(i, j int) bool {return sliceCntType[i] < sliceCntType[j]})

    sort.Slice(sliceCntContainer, func(i, j int) bool {return sliceCntContainer[i] < sliceCntContainer[j]})

    for i := 0 ; i < len(sliceCntContainer); i++{
        if sliceCntContainer[i] != sliceCntType[i]{
            res = "Impossible"
        }
    }

    return res
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 1024 * 1024)

    qTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
    checkError(err)
    q := int32(qTemp)

    for qItr := 0; qItr < int(q); qItr++ {
        nTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
        checkError(err)
        n := int32(nTemp)

        var container [][]int32
        for i := 0; i < int(n); i++ {
            containerRowTemp := strings.Split(readLine(reader), " ")

            var containerRow []int32
            for _, containerRowItem := range containerRowTemp {
                containerItemTemp, err := strconv.ParseInt(containerRowItem, 10, 64)
                checkError(err)
                containerItem := int32(containerItemTemp)
                containerRow = append(containerRow, containerItem)
            }

            if len(containerRow) != int(int(n)) {
                panic("Bad input")
            }

            container = append(container, containerRow)
        }

        result := organizingContainers(container)

        fmt.Fprintf(writer, "%s\n", result)
    }

    writer.Flush()
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}
