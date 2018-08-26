// +build ignore

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var path = "/Users/novalagung/Documents/temp/test.txt"

func main() {
	// writeFileName := "./pro_result_parse/" + filepath.Base(os.Args[1])
	// createFile(writeFileName)
	a, aMap := readFile(os.Args[1])
	b, bMap := readFile(os.Args[2])
	// writeFile(writeFileName, reachedSlice)
	fmt.Println(len(a))
	fmt.Println(len(b))
	fmt.Println(len(intersection(a, b, aMap, bMap)))
	// for _, val := range without(a, b, aMap, bMap) {
	// 	fmt.Println(val)
	// }
}

// n がスライスに含まれているか
func member(n string, xs []string) bool {
	for _, x := range xs {
		if n == x {
			return true
		}
	}
	return false
}

func intersection(xs, ys []string, xsMap, ysMap map[string]int) []string {
	zs := make([]string, 0)
	for _, x := range xs {
		if _, ok := ysMap[x]; ok {
			zs = append(zs, x)
		}
		// if member(x, ys) {
		// 	zs = append(zs, x)
		// }
	}
	return zs
}

func without(xs, ys []string, xsMap, ysMap map[string]int) []string {
	zs := make([]string, 0)
	for _, x := range xs {
		if _, ok := ysMap[x]; !ok {
			zs = append(zs, x)
		}
		// if member(x, ys) {
		// 	zs = append(zs, x)
		// }
	}
	return zs
}

func contains(s []string, e string) bool {
	for _, v := range s {
		if e == v {
			return true
		}
	}
	return false
}

func changeOrderOfRow(a, b string) string {
	if a > b {
		return b + "," + a
	}
	return a + "," + b
}

func createFile(filePath string) {
	// detect if file exists
	var _, err = os.Stat(filePath)

	// create file if not exists
	if os.IsNotExist(err) {
		var file, err = os.Create(filePath)
		if isError(err) {
			return
		}
		defer file.Close()
	}

	fmt.Println("==> done creating file", filePath)
}

func writeFile(filePath string, reachedSlice []string) {
	// open file using READ & WRITE permission
	var file, err = os.Create(filePath)
	if isError(err) {
		return
	}
	defer file.Close()

	for _, val := range reachedSlice {
		// write some text line-by-line to file
		_, err = file.WriteString(val + "\n")
		if isError(err) {
			return
		}
		// _, err = file.WriteString("mari belajar golang\n")
		// if isError(err) {
		// 	return
		// }

		// save changes
		// err = file.Sync()
		// if isError(err) {
		// 	return
		// }
	}

	fmt.Println("==> done writing to file")
}

func readFile(filePath string) ([]string, map[string]int) {
	// re-open file
	var file, err = os.Open(filePath)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	// read file, line by line
	// var text = make([]byte, 1024)

	var reachedMap = map[string]int{}
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		text := scanner.Text()

		splitedStringSlice := strings.Split(text, ",")
		if len(splitedStringSlice) >= 3 {
			floatVal, err := strconv.ParseFloat(splitedStringSlice[2], 64)
			if err != nil {
				continue
			}
			threshold, err := strconv.ParseFloat(os.Args[3], 64)
			if err != nil {
				continue
			}
			if floatVal < threshold {
				continue
			}
		}

		// dotSplitSliceA := strings.Split(splitedStringSlice[0], ".")
		// dotSplitSliceB := strings.Split(splitedStringSlice[1], ".")

		// log.Println(dotSplitSliceA[len(dotSplitSliceA)-1])
		// log.Println(dotSplitSliceB[len(dotSplitSliceB)-1])

		// a := strings.Replace(dotSplitSliceA[len(dotSplitSliceA)-1], "2gram", "", -1)
		// b := strings.Replace(dotSplitSliceB[len(dotSplitSliceB)-1], "2gram", "", -1)

		// a := strings.Replace(splitedStringSlice[0], "2gram", "", -1)
		// b := strings.Replace(splitedStringSlice[1], "2gram", "", -1)
		a := splitedStringSlice[0]
		b := splitedStringSlice[1]
		elm := changeOrderOfRow(a, b)
		if _, ok := reachedMap[elm]; !ok {
			reachedMap[elm] = 1
		}
		// log.Println(elm)
		// if !contains(reachedSlice, elm) {
		// 	reachedSlice = append(reachedSlice, elm)
		// }
	}

	// for {
	// 	_, err := file.Read(text)
	//
	// 	// break if finally arrived at end of file
	// 	if err == io.EOF {
	// 		break
	// 	}
	//
	// 	// break if error occured
	// 	if err != nil && err != io.EOF {
	// 		isError(err)
	// 		break
	// 	}
	//
	// 	splitedStringSlice := strings.Split(string(text), ",")
	// 	_, err = strconv.ParseFloat(splitedStringSlice[2], 64)
	// 	if err != nil {
	// 		continue
	// 	}
	//
	// 	a := strings.Replace(strings.Split(splitedStringSlice[0], ".")[len(splitedStringSlice)-1], "2gram", "", -1)
	// 	b := strings.Replace(strings.Split(splitedStringSlice[1], ".")[len(splitedStringSlice)-1], "2gram", "", -1)
	// 	elm := changeOrderOfRow(a, b)
	// 	if !contains(reachedSlice, elm) {
	// 		reachedSlice = append(reachedSlice, elm)
	// 	}
	// }
	keys := make([]string, 0, len(reachedMap))
	for k := range reachedMap {
		keys = append(keys, k)
	}
	fmt.Println("==> done reading from file")
	// fmt.Println(string(text))
	// log.Println(reachedMap)
	return keys, reachedMap
}

func deleteFile() {
	// delete file
	var err = os.Remove(path)
	if isError(err) {
		return
	}

	fmt.Println("==> done deleting file")
}

func isError(err error) bool {
	if err != nil {
		fmt.Println(err.Error())
	}

	return (err != nil)
}
