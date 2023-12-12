day_10_example_1 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

day_10_example_2 = """.....
.S-7.
.|.|.
.L-J.
....."""

day_10_input = """FL7-|-FJ7.J.FF-.|7.JFF|F--7LJ-F--.--|.FF77LFL..7-F|-F|--L77F7-F7FFF--7---7FFL|7FJ7|J7.FF--F|7-F-7.L|FF|.FF7-J77F7FF7FF|.FF|7F7|-F.FJJFLJJFF-
F-7.F-JF-7L7-|L-JF7--JLJJFL|.L|.L7|-7--J||.J.FL|FLL|LJL7L|-FL7.|FLJL.J7JJL7J|JL-.FJ.LJJ..||FJF--FF7|-J-FJJJ.|||J7.L|J||-|JL|-J-.LJ-7L-.|FFJJ
LFJ-LJJL-FJJ.LF7F|J.|7LJL|7.-7L-7.7.L7LLFL7|LL7LF7J|-FJFF|-7J.F-777JF7||FF7.L.F7LF77.F-7J-7..LLF7-F.7LF-J7JF--J|LF-JLLJ||FLL-JJF--L7||-FJ7--
.L|F||7L7|.FL-|7||-7-LJ77LL7|LFJ|-J.F77.L|J7.FL--JF-7LFLJ.L.|L-LJL|7LJ-JF7JFL7J7LLF7F|LL7.7-7.L|L|JFJ.7.LF-L|L77F-7F-JL7JL7L7.|L.L|.F|.L|L-|
F---F|7F--7-JFFJ-JFL7F|F.FLL-77-|-7FFJL-7LLL-7||LL7FJJF--7|FJ|FL7JF7-JL||F-FJ|J|FL|7LJJLLF|FFFJ|-|F-7|LF7|FF-7J|7LLFJ..J-JJ-J-7|.F7FFJ-.-L-7
LL-7J|L7.LLF7LLJ.FJ7LJ7JF|F7-LF-L.-7|LJ-JLL77L7JJ|LJ|FFJJLL7J7F--J|J.7-|L-FJ.|FLL.LLJJ.|-7JFFF-|.FJ-JJ-F-F7|JL--L-LJ|.FJJ.|.|LLJ7L|7|LL7J|-|
LF-L-F|LF7|L|7-JFFJ-JLF.|.L-7||-J7FL7||7.F--77|LF||.L-|J.F...F.|J|||---F7-F--|77L.|L--J-FJF--7F7JJJ.|JFL-J-|-F-FLF--77-F77F.F-|J7FLFL7F|LF-7
FL-||L7LF-|JJ|LF7JJL|7.LL7|L-FJ.LJJ7|L|7.FFF7JJ||L|7.FLF7|.|.|7LF7LF7.|.F-7J|L-7JF7.|7||JFL-7|||7-|-FFJJF7J..J.L7LJL|7.||F-7-7F-F7LL.|L77|LJ
||-F7.|JL-JJ|F-|LF..|77LL-J7--|-||L77LLLL-LJJ|JF.FJF7-F|-F.F.-7-|7.L-77-|FLJFF-7-LF.|77JFJF7|||L77J.|F7-J7.F7|F.L7.-|L|L-JF|J||J|LJ|.L7.J|.J
-|-L--7.||LJ|L|.F|-L7LLF-7J.7.JFL7-JJ7..|7-|.|.L7J|FJ.F77|7.F7.7FJ77.LJFL||.FJF|JF7F|J|..FJLJ||FJ7LF-JL7|F-7LLJJJL77|-|..F||.-J.|--7.L77|L-|
|.FLF-|-7L.FF.FF|-7.F7J|LLJ.|J|F-L-7|F7FL7F|..L.|FFF7FJ|F7L|J7|LJ-7777L-|J|7|FLL-LL7-F7-FL--7||L777L--7|FJFJ7-||--|-|.F7FLJ7J..FJ--|--JF7|FJ
J-L-7FL-J.|JJ77LLJ-FF7-F.L-77.7.||7F7|L7.LLL.7.7FF7||L7LJL77|FF7L7JJF7.FF-F-77LJFJ.7F||-F-7FJLJFJL|-F7||L7L77|F7.FFFF7||-|L77F77J..F7.|L-7|J
FLL-FJJ.|.LJ-JJ---||J|..F-7||F7-J.F|||FJ777|7F7F-JLJ||L-7FJLFFJ|LJ|.F.F7L|L7|F7L|.-LFJL7L7|L--7L7F7F||||FJFJF7||F7F7|LJ|F7|||-JJL--JJ|FJ-JJ-
L7|.L7F-F|7.F..-.F|J.LF7J-F-7||.LF-JLJL-7-F7F||L-7F-JF7-||JF7L7|7.F7|F-7-F-J|||F-7.FL-7L7||F-7|FJ||FJLJLJFJ|||||||||L-7LJL-7|.LF7-J--JL-77.|
L-|FLL7.F|77L77.F7|F7.|||L7L-||7FL-7F---JFJL7|L7FJ|F7|L7||7||.|L7-F7FL7L7L-7LJL7.FF7|FJFJ||L7LJL7||L7F---JF-JLJ||LJ|F-JF7F-J7.FJL7LFL7L.LFFJ
|J|7.L|F||F77-7-|-7LL7||7F77|||F-7FJL7|F7L-7||FJ|FJ|LJFJ|L7||FJFJFJ|F7|FJF-JF--J.FJ|FJFJFJL7L--7LJ|FJ|F-77|F---JL-7|L7FJLJF77-L7F77|L|7|7JJJ
LFJ--.LLJ7FJLLFJ..F-|7||FJ|F7||L7||F7|FJ|F7|||L-JL7|F7L7|FJ||L7L7L7||LJL7L-7L--7-L7LJFJFJF-J-F7L7FJ|FJL7|FJ|FF7FF7|L7|L77FJ|JFF7JL-L7.F||FFJ
FJJ-JFL|-LJ|.L|.L-L-F7||L7LJ||L-J|||LJL7||||LJF---JLJL7LJ|FJ|FJFJFJ|L7F-JF7L7F7|F7|F7L7L7L7JFJL-J|FJL7.||L7L-JL-J|L7|L7L7|FJFFJ|FF7|7LJJ-|JJ
-LJ7.LF-.L77.F7F7F||||||.L-7|L--7|||F7FJ|||L-7L-7F-77FJF-JL7LJFJLL7|7||F7||FJ|LJ||LJL7L7L7L7|F--7LJF7L7||J|F-7F--JFJL-JFJ||F7|FJ-7-|7|F|J||7
.L--7J|L-LL77|7||7F7|||L--7||F--JLJ||||FJ||F-JF-JL7L7L7||F7L-7L-7FJL-J||LJ|L7L7FJL7LLL7|FJFJLJF-JF7|L-J|L7|L7|L7F7L--7FJJ||||||7.L.LL-JJLF--
..|.F7|L7J|L-L--F-|LJLJF7FJ|||F---7||LJL-J|L-7|-F7L7|FJL7||F-JF-JL-7F-J|F-JJL7LJF-JF--JLJFJF7JL-7|LJ|F7|FJL7|L-J||F77||F7|||||L-7.7-FL7|F-J7
.F|JL||F|--7-7-LJLL-7F-J||-||LJF7FJLJF7F--JF7||FJL7||L7FJ||L7FJFF-7|L-7||F7F7|F-JF7L---7FJFJL7F7|L-7FJ|||F-JL7F7||||FJLJ||LJLJF-J7.FFJF.||F-
7FJ-7L-FJJLL-J|L-7F-J|F-JL-JL7L||L---J||F7FJ||LJF-J|L7|L7||FJ|F7L7|L7FJ|||LJ|||F7||F7JFJL7L7FJ|LJF-J|FJ||L-7FJ|LJLJ||F--J|F---JJFJ-LJFL-F7||
FJJ|JJ||7.L|FL7.FFL7FJ|F7F--7L7|L-----JLJ||FJL-7|F7L7||FJ|||FJ|L-J|FJ|L|||F-J||||||||FJF-JFJL7L-7L7FJL7||F-JL7L-7F-J||7F7||F7F-77.7LFL7LLJ|F
|7LFFJ|F-..LJF77L|7LJ.LJLJF-JFJL--------7LJ|F7FJ|||FJ|||J|||L7L--7||FJFJ||L-7|LJ||LJ|L7L-7|F7|F-JFJ|F-J||L-7FJF7|L--JL-JLJLJLJFJJ7LFL-J..LL|
L-FJLFJLJ.L.L-LJLLF7F7F--7L-7L-7F-7-F7F7L7FJ||L7LJ|L7LJ|FJ||FJLF-J||L7L7LJF-JL-7|L-7|7|F-J||LJL-7L7|L7FJL7FJL7|LJF-7F7F7F7F--7|J|.FF7F7F7JF-
L.|-|.-.L|.F7J|7.F||||L-7|F7|F-JL7L-J|||FJ|FJ|FJF-JFJF-JL7|||F7|F7|L7L7L7FJF---J|F7|L-J|F7||F7F7L7|L7||F-JL-7||F-JF|||||||L-7LJLL-F--J-F7-|.
J7LFF--F.-7||F77-FJLJ|F7||||||-F7L--7|||L7||FJL7L7-L7L-7FJ|||||LJ||FJFJ-|L7L---7|||L7F-J||||||||FJL7|||L7F7FJLJ|F-7LJLJ|||F7L-7||-FJJ|LLL-L-
LL7|||LL7J-F-JL7FJF-7||LJ||LJL-J|F7L||||FJ||L7-|FJF7|F-JL7||LJL-7||L7|F7L7L-7JFJ||L-JL7FJ||LJ||||F-J|||FJ||L7F-JL7|F7F7LJ|||F7L7F-77FL..LF-J
||FLJ|F7|LFL--7|L-JFJ|L-7LJF--7FJ||FJLJ|L7|L7L7||FJLJL7F7|LJF---J|L7|||L7|F-JFJFJL7F-7|L7|L-7LJ|||F7||||FJL7|L7F-JLJLJL-7LJLJL-J|FJ-7F7J-JJ7
7-F77FLF|-F7F-J|F7FJFJF7L--JF7||FJ|L--7|FJL7|FJ||L---7||||F-J-F-7|FJ||L7|||F7L7|F-JL7LJFJL-7L7FJ||||||||L7FJ|FJ|F7F7F---JF-7F7F7|L--7JLJ.J7|
-7LL7F.-F-J|L-7|||L7L7||F--7|LJ|L7|F7FJ|L-7|||FJ|F7F7|||||L7F-JFJ|L7|L-J||LJL7||L-7FJF-JF--JFJL7|||||LJL7||-|L-J|LJLJ-F7FJFJ|LJ||F7FJ--.L-77
L-.LJJ7.L-7L--JLJL7L7|||L-7|L-7|FJ|||L7L7FJ||||FJ|||||||||FJ|F-JFJFJL--7||F--J||F-J|.L-7|F-7|F7LJLJLJF--J||FJF7FJFF7F7||L7L-JF7LJ|LJFF.|.F7|
||L-|J.F--JF-7F7F7L-JLJL--JL7L||L7||L7|FJL7|||||FJ||||LJ|||FJL77L7|F7F7|LJ|F7FJ|L-7L7F7|LJFJLJL--7F--JF-7|||FJLJF-JLJLJL-JF--JL7FJ7FLLJ.L-|J
J-JL-7-L-7FJFJ|||L7F-------7L-J|FJ|L7|||F7|||||||FJ||L7FJ|||F-JF7||||||L7FJ||L7|F7L7|||L-7|F7F7F7||7F7L7||LJL7F-JF7F-7F7F7L---7LJ.L7|.|-|||J
.L7..F-F-JL7L-JLJ|LJF-7F7F7L--7|L7|FJ||||||LJLJ|||FJL7|L7|||L7FJ||||LJ|FJ|FJL7|LJL-J|||F7|||||||LJL7|L7|LJF--J|F-JLJ-|||||F7F-J||-L-|7.LF|.F
7-|-|||L-7FJJF--7F-7L7||LJ|7F-JL-JLJ-LJ|||L--7FJ||L-7||FJ|||J||.||||F-JL7||F7|L7F---J|||LJ||LJ|L-7-LJJLJLFJF--JL7F7F7LJLJLJ||F7JLFFLJ||7FJ7L
|||.|FFJJ||FFL-7|L7|FJLJF7L7L---------7|||F--J|FJL7FJLJL7|||FJL7||LJL-7FJLJ|LJFJL7F7FJ|L-7LJF7|F7|F------JFJF7F7LJLJL7F7F7JLJ||L7J--7|J7--LJ
7-J-J-J7FLJFF--JL-JLJF--JL7L---------7|||LJLF-J||FJL---7LJ|||F7||L--7FJ|FF-JF7|F-J|||-|F-JJFJLJ||||F7F7F--JFJLJ|F-7F7LJLJL-7FJL7JFFLLJFL7.L|
L--FJ|-|7F--JF------7|F---JF7F-7F7F-7||||F--JF7L7L7F7F-J-FJ||||||F--JL7L7L-7|||L7FJLJFJL7F-JF7FJLJ||||LJF--JF77|L7LJL------J|F-JFJ-F.|7L|F-7
L|||-JLL7L--7|F-----J|L-7F7|||FJ|LJFJ||||L7F7||FJFJ|LJF--JFJ||LJ|L---7|FJF7||||L|L7F-JF7|L7FJ||F-7||LJF7L-7FJL7|FJF77F7F-7F-JL--77J.L.-.L7.|
F--J||.L7JF7LJL--7F-7L7FJ|||LJL7|F-J7LJLJLLJ||||7L7|F7|F-7|L|L-7|F--7|||FJLJ||L7L7|L-7||L7LJFJLJFJ||F-JL--J|F-JLJL|L7|||FJ|F----JF77.|L7LJ7L
|.|L777FFF|L----7LJFJFJL-JLJF--J||F7F7-F7|F-J|||F7LJ||LJFJ|FJF-J|L-7||||L-7FJL7L7||F-J|L7|F-JF7FJL||L-7F---JL--7F7L7||LJL7||F--7-||LJJ-|.LJJ
L-77.FL|LFL----7|F-JFJF-7F7FJF--JLJLJL-JL7L7FJ|LJL--JL-7L-JL7L-7|F-JLJ|L-7|L7L|FJLJL-7L7LJL7FJ|L7FJL7FJ|F--7F-7LJL-JLJF--J|||F-JFJ|7|-F|-7|J
L|J77.||-F-7F7FJLJF7L7L7LJ|L-JF7FF----7F7L7|L7|F7F---7FJF---JF7||L---7L--JL7L7|L---7LL7L-7JLJFJFJL7FJL-JL7|LJFJF-----7L---JLJL7FJFJF7LLL-J7|
F7F7-|-7.L7LJLJF7FJ|FJ-L-7L---JL7L---7||L7||FJ||LJ7F-JL7L--7FJLJL7F--JF----JFJ|F7F7|F-JF7L7F-JFJF-J|F-7F7L--7L7L---7|L-7F-7F-7LJFJJ||-|L--77
-J-L7J|JFF|F---J||-||F---JF7F--7|F7F-JLJF||||FJL--7L--7L-7FJ|F7F-JL--7|F7F-7|.||||||L-7|L7||F7L7|F-JL7LJL---J.L-7F7L--7LJ7LJ7L-7L--J|77-J-|7
J.FJL-|7JFLJF---JL7LJL7F--JLJF7|||LJF---7||LJL---7L--7|F7|L7LJ|L7F7F7|||||FJL7LJ|||L-7|L7|||||FJ||F-7L---7F7JF7F||L7F7L---7F--7L7F7FJ7JLJ--7
F-L.|JJF77J-L---7FJF-7LJF----J|||L--JF--JLJJF7-F7L---JLJ||FJF7|FJ|||LJLJ||L7FJ-FJ|L7FJL-J||LJ|L7LJL7L----J|L-JL7|L7|||F7F7LJF-JL||LJLL-77F|J
|J-|L-FJ|LF7F-7FJ|-L7|F7L----7LJL---7L-7F7FFJL-JL7-F---7||L7|||L7||L-7.FJL7||F-JFJFJL7FF7LJF7|FJLF7L------JF--7||FJLJLJ|||F7L--7||J|||||F77J
7-7FJ|L7L-J|L7|L7|F-J|||F7F-7L-7F--7L-7LJL-JF7F-7L-JF--J|L7|||L7||L-7L7L7FJLJL-7|7|F7L-JL7FJLJ|F7||FF-----7L7LLJLJ-F--7||||L7F-J||77|FFLJL7|
L-|7L--L--7L-JL-J|L-7|||||L7L--JL77L-7L-7F-7|||LL7F7L--7L-JLJ|FJ|L-7L7|.|L--7F-JL7|||F7F-JL--7||LJL7L--7F7L-JF7F7F7|F-JLJ|L7LJLFJL-7JF|-F-F7
F7.JJFF-7F|F7F7F-JFFJLJLJL-JF--7FJF--JF-JL7LJ|L-7||L---JF7F7FJ|FJF-JJ|L7|F7FJL7F7|||||||F7F7FLJL7F7L-7LLJ|F--JLJLJLJL---7|FJF7FL7F-J-7|.-.|J
LJF.FLL7|FLJ||||F--JF-7F-7F7|F-JL7L--7L---JF7L-7||L-----JLJ||FJL7L--7|FJLJ|||F||LJLJ||LJ||||F-7JLJL-7|F7LLJF---7F7F-----JLJ-||F7LJ7J7|7F|7|J
LF.F-LFJL---J|LJL7F7L7LJ7LJLJL---J.F-JF7F--JL-7|||F7F----7FJ||F-JF7FJ|L7F-J|F-JL--7|LJF-J|||L7|F7F7FJLJL--7L--7LJ|L--77F7F-7|LJL7-F.FFF7JFL7
LJ-JJL|F7F7F7|F7|LJ|FJF----------7FJF7|||F7F7FJLJLJ|L---7LJ7||L-7|LJFJFJL7FJL7F-7FJF--JF7LJL-JLJLJLJF7F7F7L--7L-7|F-7L7|||FJ|F--J7JLF-7J7JJ|
FL7|7JLJLJLJLJ|L---JL7L--------7FJL7|LJ|||LJ|L----7|F---JJF-J|F-JL7-L-J7-|L7FJL7||||F-7|L---------7FJLJLJL--7|F-JLJ-|FJ|||L7|L77-FF-J.|FJ.FL
|-JF-JFLF7F---JF-7F7FJF--------J|F7LJF7LJL7FL---7FJLJF7LF7L-7||F7FJLLJFL-L7|L7FJ||FJ|.LJF---------J|F-------JLJF-7F7LJJ|LJFJ|FJFF77-J-|-J7..
L7||.F|L|LJF7F7L7LJ||L|F7F-----7LJL--J|F--JF7F7.|L7F-JL-JL77LJLJ||F7JJF.|-||-|L7LJL-JF-7L-------7F-JL----7F7LF7L7LJL7F-JF7L-JL--JL7||.|77F77
L7-JFLFJL7FJLJL-JF-JL7LJ||F----JF----7LJF--JLJL7L-JL7F----JFF-7FJLJL-7----||7L7|F|J|LL7|F------7LJF--7F-7LJL-JL-JF--J|F-J|F7F-7F7FJ777F|7JF|
FJJL|J..LLJLF---7L---JF-J|L7F-7FJF---JF7|F-----J|F-7|L7F7F77|FJL-7F7FJ.FJ-LJFLLJJJLFF-JLJF7F7F7L-7L7FJL7|F-7F-7F7L---JL-7LJLJFJ|LJJ||-FLJ.LL
F7.-|..F|.|LL--7L----7L7FJ.||FJ|FJF--7||||F---7F7L7LJFJ|LJL-JL7F7|||L7J7-LJ-7JFJ.F7FL--7FJLJ|||F7L-JL--JLJ.LJJ|||F7F-7F-JF7F7L-JJ|FFJFJ|LFJ|
|-J||.FL-7LF7F7L----7L7||F-J|L-JL-JF7LJLJLJF--J||FJF-JF|F-7F-7LJ|LJL-J-F.FLFF7|L7JLJLF-J|LF7LJLJL--------7F--7LJ|||L7|L--J||L77--|FJ-J7|7F77
7.LLF7J..F7||||F7F7||FJLJL--JF---7FJL7F-7F7L-77|||FJF--JL7|L7L--J.F--77F-7L||7J.|F|7LL-7|FJL7F7F7F-7F----J|F-JF7LJL-JL-7F-JL7|F7|L|JLF|JL-F-
|-FLJ|FFFJLJLJLJLJ|FJ|F7F7F7FL7F7|L-7LJ-LJL--JFJLJL-JF---JL-J.F7F7|F-J7|FLF|J.|FFL|JJF|LJ|F7LJLJLJFJL-----JL-7||F7JF7F7LJF7FJLJL--77--77J-|J
F---7L-F|F------7FJL7LJ||LJL-7LJ|||FJF7F7F7F--JF7F7F7L-7JF7F--JLJLJL7J-LJF7JFF--F-JJ-FLJ7LJL7F---7|JF7F7JF7F7|||||FJLJL7F||L7F----JJ-|LL7JL7
L-||L7|FLJF7FF7FJL7|L7FJL--7FJF-JL7L7|||LJLJF7FJ||||L-7L-J||F----7F-J|FLJ|J.L7J.JJL7.||LF7F7||F--JL-JLJL-J|||LJLJLJF---JFJL-JL7F--7LFLJF--77
|-F7.LL.LFJL7||L-7|F-J|F7F7|L-JF-7L-J||L7F--JLJ.LJ|L-7|F-7LJL--7JLJ|LL7.L|7-|FJL|.LL-|7F|LJ|LJL--7F7F----7||L7F---7L7F--JF-7F7LJF-JF7|FLJ.JJ
|FLJF-JF-L-7LJL--JLJF7LJLJLJF-7|FJF-7|L-JL------7FJF7|||F|F-7F7L-7.77JL7.--.FJ7F|-7|-F7FL-7L----7LJ||F---JLJ|LJ.F7L-JL7F-JF||L--JF7|L-7LL7.-
L||.|.F|J|FL----7F7FJL--7F-7L7LJL-JFJ|F---7F--7FJL7||||L7||FJ|L7FJ7|-7FF-7J7|J|FJ7|7.|L--7L-7F-7L--J|L-----7FF--JL-7|FJL-7FJL----JLJF7|7.7-.
FJF|-LLJLF-----7LJ|L7|F7LJLL-JF-7F7L-JL--7|L7J|L-7||LJ|FJLJL7|L||F77-|7--L7F--J|L7.|-L7F7L--JL7L7F-7|F-----JFJF7F-7L-JF7FJL-7F7F7F7FJLJJ7J-7
.-|||.J7F|F---7L--JFJFJL------JFJ||F7F7F7|L7L7|F-J||F7LJ.F-7|L7|LJ|J-J|JFLJJJ..F777JJ.LJL--7F-JFJ|-LJL------JFJ|L7L-7FJ|L7F7LJLJ||LJ7-|7|7.L
|F7-|-|L|LJF7FJF---JL|F-7F7F7F7L-JLJLJLJLJFJFJ|L-7LJ|L-77L7LJFJ|F-JJL7|FFJ||F77F.||.FFFLF--J|F-JFJF---------7L7L7L-7LJFL-J|L7F-7LJJF77J-|-|.
77|F|-L.LLJ|LJFJF-7F7LJ7LJLJLJL7F-----7F-7L7|FJF7L7FJF-JF7L-7|FLJLL-7.FLJ7--7JF|.FL-FL--L---JL--J-L--------7L7L7|F-JF7F7F7|FJ|FJF-7|L7L7JF-J
L7JFJFJ7.LFJF7|LL7LJL----------J|F---7LJFJFJ||FJL-JL7|F-JL7FJL7F|L||JFL.F|F|L--J.7J-7..FF7F7F----7|F7F7F7F-J|L7|LJF-JLJLJLJ|FJL7|FJ|FJ||FL7|
7|FJF|7L-|L7|LJF7L-7F--------7F-J|F7LL--JFL-JLJF7F--JLJF7FJL--J-J-F7--.--FL|7J|7-FJF7.F-JLJ|L---7L-J||LJLJF7F7LJF-JF-7F---7LJF7LJ|FJL77-||FJ
LFJF7.FJ.L-LJF-JL-7LJF7F----7LJF7LJL---7F7-F-7J|LJF7F7FJLJLF-7F|J.|L..|JFL7FJ--F7F7|L7L---7L--7JL--7|L----JLJ|F-JF-J.|L--7L7FJL-7LJF-JF7FFJ-
LJL|JF--||FF-JF7F7L--JLJF--7||FJL-----7LJL-JFJFJF-JLJLJF7F7|FJ7F7-77FF7F--JJ7|L|||||FJF7F7L--7|F--7||F------7||F-JFF7L7F7L7|L--7|F7L--J|7J7|
F|..F77L-F7L-7|LJ|F-7F-7|F-JL-JF7F-7F7L-----J|L7|F7F7F-JLJLJL-7||7LJ7|L7JLJ|-F-J||||L7||||F7FJ|L-7LJLJF----7LJ|L---JL7|||FJ|F7FJLJ|F7F7|J.-7
L.L-7L77L|L--J|F-J|FJ|7LJL-7F-7|LJ-LJL7FF7F7F--JLJLJLJF----7F-J||F7LFJFJ.7|F7L-7||||FS||||||L7|F-JF7F7|F---J7FJF-7F7FJLJ||JLJ|L--7LJLJLJ.7J7
L|.J|FFJ.|F-7FJL7FJL7|F-7F7LJJLJF----7L-JLJLJF-7F7F7F7L---7LJF-JLJL7|FJJ.7-F-7FJ|||||FJLJ|||FJ|L--JLJLJL--7F7L7|7LJLJF7JLJF-7|F--J-||FJJFF.F
FL7-JJ|77LJF|L7-LJF7LJL7LJL--7F7L---7L7F7F7F7|FJ||||||F7F7L-7|F-7F-J||JF--7|FJL7LJ|||L--7LJ|L7L7F---------J||FJL-----JL---JFJ|L-7-JJF-JFL|-F
|L|.JJL7-JLFJFJF-7|L--7L----7LJL----JFLJLJLJLJL-JLJLJLJLJL7FJLJFJL7FJL7L-7LJL-7|F7LJL7F7L-7|7L7|L---7F-----JLJF7F-7F7F--7F7L7|F7L7J..JJJJL7|
JLLJJ|7||7|L7|FJFJL--7|F--7JL7F--7F7F7F----7JF7|F-------7.LJJJ.L7FJL7FJF7L-7F-JLJL--7LJL--J|F7||F7F-J|F----7F7||L7LJ|L-7|||FJ||L7|-77JLLJFF7
.F7..LF7-|J-||L7L-7F7||L7FJF-J|F-J|LJLJF---JFJL-JF-7F7F7L-7JFF|L|L7J|||||F7|||F77F-7L-----7LJ|||||L--JL---7LJLJL7L-7|F-JLJ||.LJ|LJ7.FFJLJ--J
LF-JJJ.FF77FLJLL-7LJLJL-JL7|F-JL--JF7F-J-F7||F--7L7||LJ|F-JF-7F7L7L7||FJLJ|||FJL7L7|F--77FJF7LJLJL--------JLF7F7L--JLJ-F7.LJ7F7JLL|7.JJL.FJ|
|L-|7FLJ|L-7F7.F7L--7F7F7FJLJF7.F--JLJF--JL-JL-7L-J||F7LJF7L7||L7|FJ||L--7||LJF7L7||L-7L-JFJL---7F--7F-7F7FFJLJL--7F7F7||F7F7||-7J|F777L7JFJ
J7JF|-7FL-7||L-JL--7||LJ||F--JL7|F-7LFJF7F7F-7FJF7.LJ||JFJ|FJ||FJ|L7|L7F-J|L-7|L-J||F-JF7FJF----J|F7||FJ|L-JF--7F7LJLJLJLJLJLJL7|--JF77L7-JJ
LF7J|.LJLL||L----7FJ||F-J|L--7FJLJ7L-JFJLJ|L7LJFJL7F-JL7L7|L7LJL7|FJL7|L-7L--JL7F-J|L--JLJFJF7F-7LJ|LJL-JF7FJJFJ|L-------7F---7L-77JJL.FJF|J
F7|7JFFF7FJL-----JL7LJL-7L---JL7F77F-7L--7L7L--JF-JL--7L-JL7L--7|||F7||F7|F--7FJL-7|F7F-7|L-J||FJF-JF----JLJF7L7L7F-----7|L7F7L--J777|-|-J|.
FF----7||L-7F7F7F-7L7F7L|F---7FJ|L-J||F--J7|F7F-JF7F-7L-7F-JF--J|||||||||LJF-J|F7FJLJ|L7|F-7FJ||FJJFJF7F----JL7L-J|F--7FJL-J|L-7F7F-7F77FLL7
-L-7F7|||F7LJ||LJLL7LJL-J|F--JL7L---7||F--7LJLJLFJLJFJF-JL-7L--7||||||LJL-7|F7LJ|L-7FJFJ||FJL-JLJF7L-J||F-----JJF7|L-7LJ-F-7|F-J|LJFJ|L77-J7
LL.LJ|LJ||L-7LJF77.L7F-7FJL---7L----JLJ|F-JF-7F7|F--JFJF---JLF-JLJ|||L--7FJLJ|F-JF7||7L7||L7|F-7J||F7LLJL----7F7|||F7L--7L7LJL7FL-7|F|FJ---F
-.7J.L-7LJF-JF-JL7F7LJFJ|F----JF-7F----JL-7|FJ|LJ|F7FJFJF--7FJF--7|||F7FJ|F7FJL-7|||L7FJ||FJFJFJFJLJL7F------J|||LJ|L---JFJF7FJF7FJL-J|-L|F-
|F|.F-7L-7L-7L--7LJL-7L-JL-----JFJ|F------J|L7L-7||||FJFJF-JL7|F-J||||||FJ||L7F7||||FJL7|||FJFJ-L---7|L7F7LF7J|LJF-JF7-F-JFJLJFJLJF7F-J..|-J
LFFFJFJF7|F-JF77L---7|F7FF7F7F-7L-J|F7F7LF7|FJF7|LJ|||FL7L-7JLJL-7LJLJLJ|FJL7||LJ||||F-J||LJFJF7JF--JL7LJ|FJL-JF7L--JL-JF-JF77L7F-JLJ|L-|||.
|F.L7L-JLJL--JL77F7FJLJ|FJ|||L7|F-7||LJL-JLJ|FJ|L-7||L7-|F-JF7F-7L7F---7LJF-J|L7FJLJ|L-7||F-J-|L7L-7F-JF7LJF-7FJ|F7F-7F7L--JL-7|L-7J77|-|J-J
F.7.L7F7F-7F7F7|FJ|L--7|L7LJL-J|L7|LJF7F----J|FJF7|||FJFJ|F7||L7L7LJF77L-7|F7|FJL7F-JF-JLJL--7L7|F7||JFJ|F-J.LJ-LJLJFJ|L7F7F-7LJF-J|FL|-|.F|
L-F7F||||FJ|LJ|||FJF7FJL-JF-7F7L-JL-7||L-7F--J|FJ||||L7|FJ|LJL7L7|LFJ|F7FJLJLJ|F7||F7L-7F-7F-JJ|||||L7L7|L----7F---7L7L7LJLJFJF7L7F7-|J.7F|J
-7|L-J|||L7|F-JLJL-J|L---7L7||L7F7F7LJ|F7||F--J|FJ|LJFJ|L7|F--JFJ|FJFJ||L7F---J|||||L-7||FLJF7FJLJ||FJFJL-7F7FJL7F-J7L7L---7L-J|FJ|||L-|.LJF
LFL-7FJ|L7LJL7F-7F-7L----JFJLJFLJLJL-7LJ||||F7FJL7|F7L7L7LJL7F7L7|L7L-J|FJL---7||||L-7LJL7F7||L--7|||7L--7LJLJ7FJL-7F7L-7F-JF--JL-JL77JJ|7FJ
.|J|LJ.L7|F--J|FJ|FJF7F7F-JF---------JF7LJ|||||F-JLJL7|FJF--J||FJL7L-7FJ|F7F--J|||L7FJF7FJ|LJL7F-J|||F7F7L---7FJF--J|L-7|L-7L7F7F7F7L777LJ-J
F|-|-LL-LJ|F-7|L7||FJ||LJF7|F-------7FJL7.||||||F7|F7|LJFJJF7|||F-JF7||.LJ|L-7||||FJL-J||LL-7FJL-7||||||L----J|FJLF7|F-JL-7L7||||||L7|7|.LJJ
LJ|..|7FLFJ|FJ|FJ|||FJ|F-J|LJ-F7|F--JL7FJFJ||||||L-J||F-JF7|||LJL-7|LJ|F7FJF-JFJ||L7F7FJL-7FJL7F7|LJ|||L------J|LFJ||L---7L-JLJLJ|L7|L-77J|.
FFF7-L77|L7|L7|L7|LJL-J|F7L---JL-JF7F7||||FJ||||L-7FJ||F7||||L--7FJL-7||||FJF7L7||FJ||L7F-J|F-J||L-7|||F7F--7F7L7|FJ|F---JF7F-7F7|FJ|F7|JF77
77|L7J.|7LLJJLJFJ|F----J|L7F-7F7F7||||||FJ|FJ||L7FJL7||||||||F7FJ|F7FJLJ|||FJ|FJ||L7|L7|L7FJL7FJL7FJLJ|||L-7||L7LJ|FJL----J|L7LJ|LJL||LJ.JJF
LFLJF-FL-JLLLF-JFJL---7FJFJ|FJ|||LJLJ||LJFJ|FJL7||-FJ|LJ||||LJ|L7LJ|L-7FJ||L7||-||L|L7|L7|L7F||F7||F7FJ||F7||L7|F7LJF7F7F--JFJF7|J-FJ|FL|J.F
||-||--J|LL|7L-7|F----J|-L7|L7|LJF---JL-7L7|L7FJ|L7L7L7||||L77L7L7.|F7|L7||FJ||FJ|FJFJ|FJ|FJFJLJ||||LJFJLJLJ|FJ|||F-JLJLJF7FJFJ||L-L-JJ.J-L-
7J--J|J-77|F-F7|||F7F-7|F7LJFLJF7L7F7F7FJFJ|FJ|7|FJ7L7L7||L7|F-JFJFJ|||7||||J||L7|L7L7||FJ|-L7F7|LJ|F7L--7F-JL7|||L------JLJFJL||J7FLL.F-F|L
LFLL-77.LFL7-||||LJLJFJ||L-----JL-J|||LJ.L-JL7L7|L7F-JFJ||FJ|L-7|FJFJ|L7|||L7|||||FJFJ|||FJF7|||L-7LJ|F7FJL7F7||||F7F---7F7FJ7F|L7J77FJJF|JJ
77J|.|7FFL-F-JLJL7F--JFJ|F7F7F-7F--J|L--7F---JFJ|FJL-7L7||L-JFFJ||FJL|FJLJL7||L7LJ|FJ-||||FJLJ|L--JF7||LJF7LJ||LJ|||L--7LJ|L7F-|FJJ|FL7FL|L-
LL-FJ7LJL|FJF-7F7|L7F7|JLJLJLJFJ|F--JF-7|L--7FJJLJF--JFJLJFF--JFJ||F-JL---7LJL7|7FJL-7LJLJL7F7L---7|LJ|F-J|F7|L7FJ||F-7L-7L-J7|LJJ|FF7L|LJ.|
|.F-J.FL-LL-JFJ|LJ-LJLJF7F7F7FJFJL7F7L7LJF--JL---7L--7|F-7FJF7FJFJ|L7F7F--JF--JL7|F7FJF---7LJ|F--7||F7LJF7LJ|L-J|FJ|L7|F-JF---7J.LF-JL7JL77J
|-F|-L--LL7.FJFJ7|F7FF-JLJLJLJFJF-J|L7L-7L7F-7F7FJF--JLJFJL7|LJ-L7|FJ||L--7L-7F7|||LJ-L7F7L--JL-7||LJL7FJ|F7L-7FJL7|FJ|L--JF--JF7LF-FL77FJ77
FFLJ7.|..|F-JFJ.F-JL7L-----7F7L7L-7|FJF-JL||FJ|LJLL7F--7L-7|L-7F7||L-J|F--JF-J|LJ|L---7||L7F-7F7||L-7FJL7||L--JL7FJ|L7L7F-7L7|.|JJ.F|J|LF7J|
L-7JF77FF-JF-JL-|F7FJF7F7|FJ|L7L7FJ|L7L-7FJ|L7L-7LFJL7LL7FJL7FJ|LJ|F--JL7F7|F7|.FJF7F7|||FJ|FJ|LJ|F-JL7FJ|L---7-|L7L7L7|L7L7L----7-FJFL.L-7|
FLL-L7-F|F-J7F-7LJ|L-JLJL-JFJJ|FJL7|.|F7|L-JFJF7|FJF7L7FJL7|||L|F-JL-7F-J||LJ|L7L7|||LJ||L7|L7L7FJL--7LJLL7F-7|FJFJ7L7||FJLL7F-7FJ-L-JL|.|L7
|7|JF7-LLJ7L77L|J.L7F7F7F-7L-7|L7FJL7||||F--JFJ||L7||FJ|F7|FJ|FJL7F--J|F7||F7L-J7|||L-7||FJ|||FJL7F--JF-7FJL7||L7L-7FJ||L7LLLJ.LJJ7.|.FF.L-J
LL|7L|.FL-7JLJ.JFF-J|LJLJFJF7|L-J|F7|||||L7F7L7LJFJ|LJ7||LJ|FJ|F7||F-7LJLJ|||F---J||F-JLJL7|FJ|F7|L---JFJ|F7|LJFJF-JL7||FJ|L|J.FJLF-7FJJFJ77
L||7||7F|J||....LL-7L7F-7|FJLJLF-J|||LJ||FJ|L7L7FJFJF--J|F-JL7||||||FJF7F7LJ||F--7||L---7FJ|L7||LJF7F--JFJ||L7FJFJ|-LLJLJJ7-J--J..|L-JJFJLLF
7JJ|JJLJ||F-.LL7.F7L-JL7||L--7FJF7||L-7LJL7L7|FJL7L7L7F7|L7F7|||||LJ|FJ||L7FJ|L7-|||F7F-J|FJFJ||F7||L--7L7|L7||FJF7.|||LL.L7FF||F.L7LJJF7.|.
L-F|||JJF-F77.LFFJL----JLJF7FJL7|||L7FJ|F7|FJ|L7-|FJJLJ|L7||||LJ|L7FJL7||FJ||L7|FJ|||||F-JL7L7|LJLJ|F--JFJL7LJ|L-JL7-F7.|-7.|-L7|7FJJF-J|FF-
.--7FJ--7-J77-7LL--7F---7FJ||FFJ|||FJL7FJLJ|FJFJFJ|F-7FJFJ|||L-7L7||F7|||L7L-7|||FJ||||L7F7|FJL-7F-JL--7|F7L-7|F---J.|7.F7-F7F-|-7L7-7|FFJL|
|J.LLJ..7-LL7LF-L.LLJ7F-J|FJL7L-J||L-7|L--7|L7|7L-JL7LJFJFJ||F7|J||||||||-L7FJLJ|L7||LJ.LJLJL7F-J|F7F--J||L7FJ|L7J7.LF7.L-JLJ7-J|L-JJJFJJL7-
F.|..-.|.LJLJ-|J.L..F-JF-J|F-J-F7|L7L||F7FJ|FJL7F---JF7L7L7|||||FJ|||||LJF7|L-7FJFJ|L---7.F--JL-7LJ|L-7FJL7||L|FJL77J||LJ.|.LFFJFLF-J.||J.JJ
L|L77.7J7.LL7..-FJ--|F-J-FJL-7FJLJFJFJLJ||FJL7FJL7F-7|L7|JLJ|||||FJLJ||F-JLJF-JL7L7|F7F7L7L-7F7FJF-JF-JL--J||.LJJ.J7.LL7F.L.F7||LLJ.FLJJFFJ.
.|-77.|L|7..FFFLJ.FLLJFF-JF7FJL7F-JFJF-7|LJF-JL-7||FJ|FJL--7|||||L--7|||F7F7L--7L7|||||L7|F-J|LJFJF7L----7|LJ..L-F7|FF.7|F|FLJFJ-FJ-|.L.FJ-|
FJLJFLJ-|.77|-7JJ-LJJ|LL7FJLJF-JL-7L7|-||F-JF--7|||L7||F-7FJ||LJ|F7FJ|||||||F7FJJ||LJLJ7|||F7L-7L7||F--7FJ7LJ.-J-7-7-F.|F7L-J|L.F-7FL7|7F7-|
L..L-JFFJJ.-JFJJ.7.FFJJF||LJ-L--7FJ7||FJ||F7L-7LJLJL||LJFJ|FJL7||||L7LJ||||LJ|L7J|L7J.F-J||||F-J-|||L7.|L--7FL..77|.|LFJLF7|FJ|FJ7FL7LF7LJL7
L7.|.L-JL-77.7.F-F7.J7.FLJ-L77F-J|FFLJL-J||L7FJ|-LJ.LJLFJFJL-7L7LJ|FJFF|||L7J|FJ|L-J-FL-7||||L-7-||L7|.L7F-J7LFLLJ--77|7FJ7-7.F-.|JFL-JLFJJ|
|.F77-|7.F.FF-7LJLF7F-7L|J.|LLL--JFLLJ.LFJ|J|L-7|LFJF|7L7L7-LL7|..||FJ-LJ|FJ-||-|JL7J||J||LJ|F-JFLJ-LJ-LLJJ|-.7L||JFLLJJ-LJ7LF7FF|L7-FJ-L-F|
-.FJ--FJ-||-FJL---JLL-LF|.--F7|-FLF7|.FFJFJLL7FJ--JJ|7-LL-J7LFJL-7LJ77J.LLJJF|L7L--J.|.FLJF-J|JJ|-|7LJFJJ-F.|FJ.LF---LJ.|L.|7FJ7||J.F-J-J7|J
F-L7|7JF-7.F77-77J.|.-.FL.|FLJJ.|FLJLJ-L7|JJJ|L7.LJ.FJ.LL7F7LL---JJL7-777-L|LL-J.F7||FFJ.LL-7|7LL.-||7L-J7.LJ77|J.|.||FFJJF-J--LF|7.|J7..FJ7
L7LL-|.-JF-7JJ.LJ..7-||JLJJLLJ7F-7...L7|LJ.|FL-J-7L7...|.LFL7||LLLJF-JLJ7F.-7||L.|LJL7JF7.LJLJF77FL.-FJ7.F7LJ-|J7FJF7J|L-7-LJJ-F-L-7|JL-FJF|
J-FJFL7JJL-JL7.F-7.L.L|L--7JFF|||.|7-|J-JJF7JFJ7.--|7.FF7J|||JFF.FFLJ|-L7..LF|F77JFL7J-|-|J7FLFJ|J|-L77|7L7.LJJ|F7F|JJFLJ|LF-7-F-7|.|.J7||7.
FLJ.L-7.|L7.F77|FJ----|-JLJ-|J-F7LL7-7|..-|-77LJ7.||--LFJJJLJFLJ.LJ.FL.FF-7.LL-LJ-LJJ7.-7|-FJJ.-JJL7J|-J7|.--L.L|.7|LFL---77-|-JF--LL7FF-LJ|
|7F-J.-77-F7||.|||.7JF|.|.LJL|7.JJFJ.LJF|LL|7F7-|-|LJ...LLJ.-7F--||F-7LJJ||--7-JL-7.L--7FJJ|LJ-JF7J|LL-FF7-|F|7FL|---FJ7|L77-|..|L|JLLJJFF-L
|7LJLFJF-7L-F7.LLJ-L.LF77J7FF|-FJ.JJ-LF-F-FF-||FF-|.F7-||FFFJF|-FLJ|-LF|-7JLLF-|.FL77F|7..FL7.-7JJFL...F-7LL7.-JJLF7L..FF.L|-|--7FJJFL||LJ.|
--7F7JL|.|J.LJF7JLLF|FJL--777|||.7-J.FLL-7LJLLJ7|7L|J7L|FJJ7.LJL7JLL7||J-7J-J|L7--7J|-L-J.--7.L|-7.F7J7FL|JLJ-L7J.JJJF-L7..|-||LLJL7|7J||LF|
|J|-J-7L-J.FJ7LJ-----7J-LFJLJ-F7JJ-|---7L7--JJ--JFLJLL7-LJL..LL--7-L-|J.L|...J-L--L-LJJLJ.|.J--L-J|JJ--7LL7-J.LJ--LJ.L-LF.L-.FJJ.F-JL----.-L"""