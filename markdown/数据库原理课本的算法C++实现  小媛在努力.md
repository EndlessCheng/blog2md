#  数据库原理课本的算法C++实现 

_ _ [ zxy_snow ](http://www.xysay.com/author/zxy_snow) _ _ [ 写代码玩儿 ](http://www.xysay.com/category/%e5%86%99%e4%bb%a3%e7%a0%81%e7%8e%a9%e5%84%bf) _ _ 围观 _ 315 _ 次  _ _ [ 9 条评论 ](http://www.xysay.com/database-cpp-115.html#comments) _ _ 编辑日期：  2014-07-01  _ _ 字体： [ 大 ](javascript:;) [ 中 ](javascript:;) [ 小 ](javascript:;)

  
实现一些算法如下图，好久没怎么写代码了，纯粹锻炼代码能力+复习数据库原理哈。 

加高亮后一些注释木有对齐捏，桑心，不太好看了都。 

这是TEST， 

ABCDEG   
3   
A->BC   
CD->G   
B->DA 

相信学过数据库原理的童鞋都懂怎么用~~~~ 

![](http://farm8.staticflickr.com/7150/6650375367_cdd0be0983_b.jpg)

/*************************************************************** * * 数据库原理算法实现——by zxy_snow 2012.1.6 23:15 * ***************************************************************/ #include <set> #include <map> #include <queue> #include <stack> #include <math.h> #include <stdio.h> #include <stdlib.h> #include <iostream> #include <limits.h> #include <string.h> #include <string> #include <algorithm> #define MID(x,y) ( ( x + y ) >> 1 ) #define L(x) ( x << 1 ) #define R(x) ( x << 1 | 1 ) #define FOR(i,s,t) for(int i=(s); i<(t); i++) #define BUG puts("here!!!") #define STOP system("pause") #define file_r(x) freopen(x, "r", stdin) #define file_w(x) freopen(x, "w", stdout) using namespace std; const int MAX = 50; typedef vector< pair<string, string> > vss; typedef vector<string> vs; string line = "------------------------------------------"; class Attribute { public : string R; // 属性集 string att; // 求属性集闭包的属性集 vss F; // 函数依赖 vs subset; // 所有的子集 vs key; // 候选码（码）集合 vs EKey; // 超码集合 vs P; // 分解 int N; // 属性集属性个数 char now[MAX]; // 求码的时候所需要的一个变量 Attribute(){} Attribute(string R, vss F) { this->R = R; this->F = F; this->N = R.length(); } // 输入 void R_input(); // 属性集的输入 void F_input(); // 函数依赖的输入 void P_input(); // 分解的输入 void att_set_input(); // 求属性集闭包的时候的属性集的输入 // 集合操作 bool ch_in_s(char ch, string b); // 判断字符ch是否在b中 bool s_in_s(string a, string b); // 判断字符串a是否属于b bool belong_Ri(string xy); // 判断xy是否属于Ri（即分解P） string intersect(string a, string b); // a ∩b string merger(string a, string b); // a ∪b string difference(string a, string b); // a - b // 功能 string closure_attribute(string att, vss F); // 求属性集att在函数依赖F上的闭包 void get_subset(int x, int pos, int num, string R); // 求子集的一个DFS void all_subset(string R); // 求属性集R的所有子集 bool is_candidate_key( string a ); // 判断a是否为候选码 void candidate_key( vss F, string R); // 求候选码 vss minimum_cover(); // 求极小覆盖 vss right_cover(); // 求正则覆盖 bool check_connect(); // 未完成 // 判断是否满足无损连接性 bool check_dependency(); // 判断是否满足函数依赖 // 满足范式判断 bool check_2NF(); bool check_3NF(); bool check_BCNF(); string most_NF(); // 最高满足第几范式，返回1NF,2NF,3NF,BCNF // 分解转换 vs to_BCNF_connect(); // 转换为BCNF的无损连接分解 vs to_3NF_connect_dependency(); // 转换为3NF的无损连接和保持函数依赖的分解 }; // 属性集的输入 void Attribute::R_input() { cout << "输入所有的属性集(以ABCD等大写字母表示，不加空格等符号，下同）：" << endl; cin >> R; N = R.length(); } // 输入函数依赖 void Attribute::F_input() { int n; string tmp; cout << "输入关系数N：" << endl; cin >> n; cout << "输入N个关系，用A->B表示，每行一个关系:" << endl; FOR(i, 0, n) { cin >> tmp; bool f = false; pair<string, string> pi; FOR(k, 0, tmp.length()) { if( tmp[k] == '-' ) k += 2, f = true; if( !f ) pi.first += tmp[k]; else pi.second += tmp[k]; } F.push_back( pi ); } } // 输入分解个数 void Attribute::P_input() { int n; string tmp; cout << "输入分解个数N：" << endl; cin >> n; cout << "输入N个分解，每个分解一行:" << endl; while( n-- ) { cin >> tmp; P.push_back( tmp ); } } // 输入要求得的属性集闭包的属性集 void Attribute::att_set_input() { cout << "输入要求得的属性集闭包的属性集：" << endl; cin >> att; } bool Attribute::ch_in_s(char ch, string b) { FOR(i, 0, b.length()) if( ch == b[i] ) return true; return false; } // 判断a是否是b的子集 bool Attribute::s_in_s(string a, string b) { FOR(i, 0, a.length()) if( !ch_in_s(a[i], b) ) return false; return true; } //求属性集att的闭包 string Attribute::closure_attribute(string att, vss F) { string ans = att, tmp; bool used[MAX]; bool f[MAX]; memset(used, false, sizeof(used)); memset(f, false, sizeof(f)); do { tmp = ans; FOR(i, 0, F.size()) if( !used[i] && s_in_s(F[i].first, ans) ) { used[i] = true; ans += F[i].second; } }while( tmp != ans ); sort(ans.begin(), ans.end()); tmp = ""; FOR(i, 0, ans.length()) if( !f[ans[i] - 'A'] ) { tmp += ans[i]; f[ans[i] - 'A'] = true; } return tmp; } // 求属性集所有的子集集合 void Attribute::get_subset(int x, int pos, int num, string R) { if( x == 0 ) { now[num] = '\0'; subset.push_back( now ); return ; } FOR(i, pos, R.length()) { now[num] = R[i]; get_subset(x-1, i+1, num+1, R); } } void Attribute::all_subset(string R) { FOR(i, 0, R.length()) get_subset(i+1, 0, 0, R); } //判断 a 是否为候选码 bool Attribute::is_candidate_key( string a ) { FOR(i, 0, key.size()) if( s_in_s( key[i], a ) ) return false; return true; } // 求码 void Attribute::candidate_key( vss F, string R ) { vs ans; subset.clear(); all_subset( R ); EKey.clear(); key.clear(); FOR(i, 0, subset.size()) if( closure_attribute( subset[i], F ).length() == R.length() ) { EKey.push_back( subset[i] ); if( !is_candidate_key( subset[i] ) ) continue; key.push_back( subset[i] ); } } // 求极小覆盖 vss Attribute::minimum_cover() { vss MC = F; // 右部极小化 FOR(i, 0, MC.size()) { if( MC[i].second.size() != 1 ) { string s = MC[i].first; string y = MC[i].second; string t = ""; t += y[0]; MC[i].second = t; FOR(k, 1, y.size()) { t = y[k]; MC.push_back( make_pair(s, t) ); } } } // 左部极小化 FOR(i, 0, MC.size()) { if( MC[i].first.size() != 1 ) { string s = MC[i].first; string ans = ""; bool del[MAX]; memset(del, false, sizeof(del)); FOR(k, 0, s.size()) { string la = ""; FOR(j, 0, s.size()) if( !del[j] && k != j ) la += s[j]; string att = closure_attribute(la, MC); if( s_in_s(MC[i].second, att) ) del[k] = true; } FOR(j, 0, s.size()) if( !del[j] ) ans += s[j]; MC[i].first = ans; } } sort(MC.begin(), MC.end()); MC.resize( unique(MC.begin(), MC.end()) - MC.begin() ); // 去掉传递依赖 vss MCC; FOR(i, 0, MC.size()) { vss tmp = MC; tmp.erase(tmp.begin() + i); tmp.resize(MC.size() - 1); string la = closure_attribute(MC[i].first, tmp); if( !s_in_s(MC[i].second, la) ) MCC.push_back( MC[i] ); } return MCC; } vss Attribute::right_cover() { vss MC = minimum_cover(); vss MCC; bool f[2000]; memset(f, false, sizeof(f)); FOR(i, 0, MC.size()) { if( f[i] ) continue; string la = MC[i].second; FOR(k, i+1, MC.size()) if( !f[k] && MC[k].first == MC[i].first ) { f[k] = true; la += MC[k].second; } MCC.push_back( make_pair(MC[i].first, la) ); } return MCC; } // 检测分解是否满足无损连接性 bool Attribute::check_connect() { return true; } // 检测分解的函数依赖保持性 bool Attribute::belong_Ri(string xy) { FOR(i, 0, P.size()) if( s_in_s(xy, P[i]) ) return true; return false; } // 返回两个字符串的交 string Attribute::intersect(string a, string b) { string x; bool f[MAX]; memset(f, false, sizeof(f)); FOR(i, 0, a.length()) f[a[i] - 'A'] = true; FOR(i, 0, b.length()) if( f[b[i] - 'A'] ) x += b[i]; return x; } //返回两个字符串的并 string Attribute::merger(string a, string b) { string x; bool f[MAX]; memset(f, false, sizeof(f)); FOR(i, 0, a.length()) f[a[i] - 'A'] = true; FOR(i, 0, b.length()) f[b[i] - 'A'] = true; FOR(i, 0, 26) if( f[i] ) x += char(i + 'A'); return x; } // 判断是否满足函数依赖 bool Attribute::check_dependency() { FOR(i, 0, F.size()) { if( belong_Ri(F[i].first + F[i].second) ) continue; string z = F[i].first; string tmp; do { tmp = z; FOR(k, 0, P.size()) { string la = intersect(z, P[k]); la = closure_attribute(la, F); la = intersect(la, P[k]); z = merger(z, la); } } while( tmp != z ); if( !s_in_s(F[i].second, z) ) return false; } return true; } // 求两个集合的差 string Attribute::difference(string a, string b) { string tmp; FOR(i, 0, a.length()) { bool f = false; FOR(k, 0, b.length()) if( a[i] == b[k] ) { f = true; break; } if( !f ) tmp += a[i]; } return tmp; } // 判断是否满足2NF bool Attribute::check_2NF() { candidate_key( F, R ); string primary_att; // 主属性 vss MC = minimum_cover(); FOR(i, 0, key.size()) primary_att += key[i]; FOR(i, 0, MC.size()) { if( ch_in_s(MC[i].second[0], primary_att) ) continue; FOR(k, 0, key.size()) if( !(s_in_s(MC[i].first, key[k]) && MC[i].first.length() < key[k].length()) ) return false; } return true; } // 判断是否满足3NF bool Attribute::check_3NF() { candidate_key( F, R ); string primary_att; // 主属性 vss MC = minimum_cover(); FOR(i, 0, key.size()) primary_att += key[i]; FOR(i, 0, MC.size()) { if( ch_in_s(MC[i].second[0], primary_att) ) continue; bool f = false; FOR(k, 0, EKey.size()) if( s_in_s(MC[i].first, EKey[k]) && MC[i].first.length() == EKey[k].length() ) { f = true; break; } if( !f ) return false; } return true; } // 判断是否满足3NF bool Attribute::check_BCNF() { candidate_key( F, R ); string primary_att; // 主属性 vss MC = minimum_cover(); FOR(i, 0, key.size()) primary_att += key[i]; FOR(i, 0, MC.size()) { bool f = false; FOR(k, 0, EKey.size()) if( s_in_s(MC[i].first, EKey[k]) && MC[i].first.length() == EKey[k].length() ) { f = true; break; } if( !f ) return false; } return true; } string Attribute::most_NF() { candidate_key( F, R ); if( check_BCNF() ) return "BCNF"; if( check_3NF() ) return "3NF"; if( check_2NF() ) return "2NF"; return "1NF"; } vs Attribute::to_BCNF_connect() { vs result; result.push_back( R ); while( 1 ) { bool f = false; FOR(i, 0, result.size()) { vss MC; FOR(k, 0, F.size()) if( s_in_s(F[k].first, result[i]) && s_in_s(F[k].second, result[i]) ) MC.push_back(F[k]); EKey.clear(); candidate_key(MC, result[i]); FOR(k, 0, MC.size()) { bool isEKey = false; FOR(j, 0, EKey.size()) if( s_in_s(MC[i].first, EKey[j]) && MC[i].first.length() == EKey[j].length() ) { isEKey = true; break; } if( !isEKey ) { f = true; result.push_back( difference(result[i], MC[k].second) ); result[i] = MC[k].first + MC[k].second; break; } } if( f ) break; } if( !f ) break; } return result; } vs Attribute::to_3NF_connect_dependency() { vs result; vss MC = right_cover(); FOR(i, 0, MC.size()) { bool f = false; FOR(k, 0, result.size()) if( s_in_s(result[k], MC[i].first + MC[i].second) ) { string tmp = result[k]; result[k] = MC[i].first + MC[i].second; f = true; break; } if( f ) continue; f = false; FOR(k, 0, result.size()) if( s_in_s(MC[i].first + MC[i].second, result[k]) ) { f = true; break; } if( f ) continue; result.push_back(MC[i].first + MC[i].second); } candidate_key(F, R); bool f = false; FOR(i, 0, result.size()) { FOR(k, 0, key.size()) if( s_in_s(key[k], result[i]) ) { f = true; break; } if( f ) break; } if( !f ) result.push_back( key[0] ); string tmp; FOR(i, 0, R.length()) { bool f = false; FOR(k, 0, result.size()) if( ch_in_s(R[i], result[k]) ) { f = true; break; } if( !f ) tmp += R[i]; } if( tmp.length() ) result.push_back( tmp ); return result; } vss F; int main() { int op; vss MCC; vs result; string menu = "\ *************************************************\n\ * 1、求属性集att在函数依赖F上的闭包 *\n\ * 2、求所有的候选码 *\n\ * 3、求超码 *\n\ * 4、求极小覆盖 *\n\ * 5、求正则覆盖 *\n\ * 6、最高满足第几范式 *\n\ * 7、转换为BCNF的无损连接分解 *\n\ * 8、转换为3NF的无损连接和保持函数依赖的分解 *\n\ * 9、判断是否满足函数依赖 *\n\ * 10、重新输入函数集以及函数依赖 *\n\ * 11、exit *\n\ *************************************************\n"; while( 1 ) { Attribute att; att.R_input(); att.F_input(); while( 1 ) { bool f = false; system("cls"); cout << menu << endl; cout << "当前属性集为：" << att.R << endl; cout << "当前函数依赖集为：" << endl; FOR(i, 0, att.F.size()) cout << att.F[i].first << "->" << att.F[i].second << endl; cout << line << endl; cout << "请输入要进行的操作下标~" << endl; cin >> op; cout << line << endl << endl; switch( op ) { case 1: att.att_set_input(); cout << "属性集" << att.att << "的闭包为：" << att.closure_attribute(att.att, att.F) << endl; break; case 2: att.candidate_key(att.F, att.R); cout << "候选码为："; FOR(i, 0, att.key.size()) cout << att.key[i] << ' ' ; cout << endl; break; case 3: att.candidate_key(att.F, att.R); cout << "所有超码为："; FOR(i, 0, att.EKey.size()) cout << att.EKey[i] << ' '; cout << endl; break; case 4: MCC = att.minimum_cover(); cout << "极小覆盖为：" << endl; FOR(i, 0, MCC.size()) cout << MCC[i].first << "->" << MCC[i].second << endl; break; case 5: MCC = att.right_cover(); cout << "正则覆盖为：" << endl; FOR(i, 0, MCC.size()) cout << MCC[i].first << "->" << MCC[i].second << endl; break; case 6: cout << "最高满足的范式: " << att.most_NF() << endl; break; case 7: result = att.to_BCNF_connect(); cout << "满足BCNF的无损连接分解为 " ; FOR(i, 0, result.size()) cout << result[i] << ' '; cout << endl; break; case 8: result = att.to_3NF_connect_dependency(); cout << "满足3NF的无损连接和保持函数依赖的分解为 " ; FOR(i, 0, result.size()) cout << result[i] <<' '; cout << endl; break; case 9: att.P_input(); if( att.check_dependency() ) cout << "分解满足函数依赖" << endl; else cout << "分解不满足函数依赖" << endl; break; case 10: f = true; break; case 11: return 0; } if( f ) { system("cls"); break; } STOP; system("cls"); } } return 0; } 

1 

2 

3 

4 

5 

6 

7 

8 

9 

10 

11 

12 

13 

14 

15 

16 

17 

18 

19 

20 

21 

22 

23 

24 

25 

26 

27 

28 

29 

30 

31 

32 

33 

34 

35 

36 

37 

38 

39 

40 

41 

42 

43 

44 

45 

46 

47 

48 

49 

50 

51 

52 

53 

54 

55 

56 

57 

58 

59 

60 

61 

62 

63 

64 

65 

66 

67 

68 

69 

70 

71 

72 

73 

74 

75 

76 

77 

78 

79 

80 

81 

82 

83 

84 

85 

86 

87 

88 

89 

90 

91 

92 

93 

94 

95 

96 

97 

98 

99 

100 

101 

102 

103 

104 

105 

106 

107 

108 

109 

110 

111 

112 

113 

114 

115 

116 

117 

118 

119 

120 

121 

122 

123 

124 

125 

126 

127 

128 

129 

130 

131 

132 

133 

134 

135 

136 

137 

138 

139 

140 

141 

142 

143 

144 

145 

146 

147 

148 

149 

150 

151 

152 

153 

154 

155 

156 

157 

158 

159 

160 

161 

162 

163 

164 

165 

166 

167 

168 

169 

170 

171 

172 

173 

174 

175 

176 

177 

178 

179 

180 

181 

182 

183 

184 

185 

186 

187 

188 

189 

190 

191 

192 

193 

194 

195 

196 

197 

198 

199 

200 

201 

202 

203 

204 

205 

206 

207 

208 

209 

210 

211 

212 

213 

214 

215 

216 

217 

218 

219 

220 

221 

222 

223 

224 

225 

226 

227 

228 

229 

230 

231 

232 

233 

234 

235 

236 

237 

238 

239 

240 

241 

242 

243 

244 

245 

246 

247 

248 

249 

250 

251 

252 

253 

254 

255 

256 

257 

258 

259 

260 

261 

262 

263 

264 

265 

266 

267 

268 

269 

270 

271 

272 

273 

274 

275 

276 

277 

278 

279 

280 

281 

282 

283 

284 

285 

286 

287 

288 

289 

290 

291 

292 

293 

294 

295 

296 

297 

298 

299 

300 

301 

302 

303 

304 

305 

306 

307 

308 

309 

310 

311 

312 

313 

314 

315 

316 

317 

318 

319 

320 

321 

322 

323 

324 

325 

326 

327 

328 

329 

330 

331 

332 

333 

334 

335 

336 

337 

338 

339 

340 

341 

342 

343 

344 

345 

346 

347 

348 

349 

350 

351 

352 

353 

354 

355 

356 

357 

358 

359 

360 

361 

362 

363 

364 

365 

366 

367 

368 

369 

370 

371 

372 

373 

374 

375 

376 

377 

378 

379 

380 

381 

382 

383 

384 

385 

386 

387 

388 

389 

390 

391 

392 

393 

394 

395 

396 

397 

398 

399 

400 

401 

402 

403 

404 

405 

406 

407 

408 

409 

410 

411 

412 

413 

414 

415 

416 

417 

418 

419 

420 

421 

422 

423 

424 

425 

426 

427 

428 

429 

430 

431 

432 

433 

434 

435 

436 

437 

438 

439 

440 

441 

442 

443 

444 

445 

446 

447 

448 

449 

450 

451 

452 

453 

454 

455 

456 

457 

458 

459 

460 

461 

462 

463 

464 

465 

466 

467 

468 

469 

470 

471 

472 

473 

474 

475 

476 

477 

478 

479 

480 

481 

482 

483 

484 

485 

486 

487 

488 

489 

490 

491 

492 

493 

494 

495 

496 

497 

498 

499 

500 

501 

502 

503 

504 

505 

506 

507 

508 

509 

510 

511 

512 

513 

514 

515 

516 

517 

518 

519 

520 

521 

522 

523 

524 

525 

526 

527 

528 

529 

530 

531 

532 

533 

534 

535 

536 

537 

538 

539 

540 

541 

542 

543 

544 

545 

546 

547 

548 

549 

550 

551 

552 

553 

554 

555 

556 

557 

558 

559 

560 

561 

562 

563 

564 

565 

566 

567 

568 

569 

570 

571 

572 

573 

574 

575 

576 

577 

578 

579 

580 

581 

582 

583 

584 

585 

586 

587 

588 

589 

590 

591 

592 

593 

594 

595 

596 

597 

598 

599 

600 

601 

602 

603 

604 

605 

606 

607 

608 

609 

610 

611 

612 

613 

614 

615 

616 

617 

618 

619 

620 

621 

622 

623 

624 

625 

626 

627 

628 

629 

630 

631 

632 

633 

634 

635 

636 

637 

638 

639 

640 

641 

642 

643 

644 

645 

646 

647 

648 

649 

650 

651 

652 

653 

654 

655 

656 

657 

658 

659 

660 

661 

662 

663 

664 

665 

666 

667 

668 

669 

670 

671 

672 

673 

674 

675 

676 

677 

678 

679 

680 

681 

682 

683 

684 

685 

686 

687 

688 

689 

690 

691 

692 

693 

694 

695 

696 

697 

698 

699 

700 

701 

702 

703 

704 

705 

706 

707 

708 

709 

710 

711 

712 

713 

714 

715 

716 

717 

| 

/*************************************************************** 

* 

* 数据库原理算法实现——by zxy_snow 2012.1.6 23:15 

* 

***************************************************************/ 

#include <set>

#include <map>

#include <queue>

#include <stack>

#include <math.h>

#include <stdio.h>

#include <stdlib.h>

#include <iostream>

#include <limits.h>

#include <string.h>

#include <string>

#include <algorithm>

#define MID(x,y) ( ( x + y ) >> 1 ) 

#define L(x) ( x << 1 ) 

#define R(x) ( x << 1 | 1 ) 

#define FOR(i,s,t) for(int i=(s); i<(t); i++) 

#define BUG puts("here!!!") 

#define STOP system("pause") 

#define file_r(x) freopen(x, "r", stdin) 

#define file_w(x) freopen(x, "w", stdout) 

using  namespace  std  ; 

const  int  MAX  =  50  ; 

typedef  vector  < pair  < string  ,  string  > > vss  ; 

typedef  vector  < string  > vs  ; 

string  line  =  "------------------------------------------"  ; 

class  Attribute 

{ 

public  : 

string  R  ;  // 属性集 

string  att  ;  // 求属性集闭包的属性集 

vss  F  ;  // 函数依赖 

vs  subset  ;  // 所有的子集 

vs  key  ;  // 候选码（码）集合 

vs  EKey  ;  // 超码集合 

vs  P  ;  // 分解 

int  N  ;  // 属性集属性个数 

char  now  [  MAX  ]  ;  // 求码的时候所需要的一个变量 

Attribute  (  )  {  } 

Attribute  (  string  R  ,  vss  F  ) 

{ 

this  -> R  =  R  ; 

this  -> F  =  F  ; 

this  -> N  =  R  .  length  (  )  ; 

} 

// 输入 

void  R_input  (  )  ;  // 属性集的输入 

void  F_input  (  )  ;  // 函数依赖的输入 

void  P_input  (  )  ;  // 分解的输入 

void  att_set_input  (  )  ;  // 求属性集闭包的时候的属性集的输入 

// 集合操作 

bool  ch_in_s  (  char  ch  ,  string  b  )  ;  // 判断字符ch是否在b中 

bool  s_in_s  (  string  a  ,  string  b  )  ;  // 判断字符串a是否属于b 

bool  belong_Ri  (  string  xy  )  ;  // 判断xy是否属于Ri（即分解P） 

string  intersect  (  string  a  ,  string  b  )  ;  // a ∩b 

string  merger  (  string  a  ,  string  b  )  ;  // a ∪b 

string  difference  (  string  a  ,  string  b  )  ;  // a - b 

// 功能 

string  closure_attribute  (  string  att  ,  vss  F  )  ;  // 求属性集att在函数依赖F上的闭包 

void  get_subset  (  int  x  ,  int  pos  ,  int  num  ,  string  R  )  ;  // 求子集的一个DFS 

void  all_subset  (  string  R  )  ;  // 求属性集R的所有子集 

bool  is_candidate_key  (  string  a  )  ;  // 判断a是否为候选码 

void  candidate_key  (  vss  F  ,  string  R  )  ;  // 求候选码 

vss  minimum_cover  (  )  ;  // 求极小覆盖 

vss  right_cover  (  )  ;  // 求正则覆盖 

bool  check_connect  (  )  ;  // 未完成 // 判断是否满足无损连接性 

bool  check_dependency  (  )  ;  // 判断是否满足函数依赖 

// 满足范式判断 

bool  check_2NF  (  )  ; 

bool  check_3NF  (  )  ; 

bool  check_BCNF  (  )  ; 

string  most_NF  (  )  ;  // 最高满足第几范式，返回1NF,2NF,3NF,BCNF 

// 分解转换 

vs  to_BCNF_connect  (  )  ;  // 转换为BCNF的无损连接分解 

vs  to_3NF_connect_dependency  (  )  ;  // 转换为3NF的无损连接和保持函数依赖的分解 

}  ; 

// 属性集的输入 

void  Attribute  ::  R_input  (  ) 

{ 

cout  << "输入所有的属性集(以ABCD等大写字母表示，不加空格等符号，下同）："  << endl  ; 

cin  >> R  ; 

N  =  R  .  length  (  )  ; 

} 

// 输入函数依赖 

void  Attribute  ::  F_input  (  ) 

{ 

int  n  ; 

string  tmp  ; 

cout  << "输入关系数N："  << endl  ; 

cin  >> n  ; 

cout  << "输入N个关系，用A->B表示，每行一个关系:"  << endl  ; 

FOR  (  i  ,  0  ,  n  ) 

{ 

cin  >> tmp  ; 

bool  f  =  false  ; 

pair  < string  ,  string  > pi  ; 

FOR  (  k  ,  0  ,  tmp  .  length  (  )  ) 

{ 

if  (  tmp  [  k  ]  ==  '-'  ) 

k  +=  2  ,  f  =  true  ; 

if  (  !  f  ) 

pi  .  first  +=  tmp  [  k  ]  ; 

else 

pi  .  second  +=  tmp  [  k  ]  ; 

} 

F  .  push_back  (  pi  )  ; 

} 

} 

// 输入分解个数 

void  Attribute  ::  P_input  (  ) 

{ 

int  n  ; 

string  tmp  ; 

cout  << "输入分解个数N："  << endl  ; 

cin  >> n  ; 

cout  << "输入N个分解，每个分解一行:"  << endl  ; 

while  (  n  \--  ) 

{ 

cin  >> tmp  ; 

P  .  push_back  (  tmp  )  ; 

} 

} 

// 输入要求得的属性集闭包的属性集 

void  Attribute  ::  att_set_input  (  ) 

{ 

cout  << "输入要求得的属性集闭包的属性集："  << endl  ; 

cin  >> att  ; 

} 

bool  Attribute  ::  ch_in_s  (  char  ch  ,  string  b  ) 

{ 

FOR  (  i  ,  0  ,  b  .  length  (  )  ) 

if  (  ch  ==  b  [  i  ]  ) 

return  true  ; 

return  false  ; 

} 

// 判断a是否是b的子集 

bool  Attribute  ::  s_in_s  (  string  a  ,  string  b  ) 

{ 

FOR  (  i  ,  0  ,  a  .  length  (  )  ) 

if  (  !  ch_in_s  (  a  [  i  ]  ,  b  )  ) 

return  false  ; 

return  true  ; 

} 

//求属性集att的闭包 

string  Attribute  ::  closure_attribute  (  string  att  ,  vss  F  ) 

{ 

string  ans  =  att  ,  tmp  ; 

bool  used  [  MAX  ]  ; 

bool  f  [  MAX  ]  ; 

memset  (  used  ,  false  ,  sizeof  (  used  )  )  ; 

memset  (  f  ,  false  ,  sizeof  (  f  )  )  ; 

do 

{ 

tmp  =  ans  ; 

FOR  (  i  ,  0  ,  F  .  size  (  )  ) 

if  (  !  used  [  i  ]  && s_in_s  (  F  [  i  ]  .  first  ,  ans  )  ) 

{ 

used  [  i  ]  =  true  ; 

ans  +=  F  [  i  ]  .  second  ; 

} 

}  while  (  tmp  !=  ans  )  ; 

sort  (  ans  .  begin  (  )  ,  ans  .  end  (  )  )  ; 

tmp  =  ""  ; 

FOR  (  i  ,  0  ,  ans  .  length  (  )  ) 

if  (  !  f  [  ans  [  i  ]  \-  'A'  ]  ) 

{ 

tmp  +=  ans  [  i  ]  ; 

f  [  ans  [  i  ]  \-  'A'  ]  =  true  ; 

} 

return  tmp  ; 

} 

// 求属性集所有的子集集合 

void  Attribute  ::  get_subset  (  int  x  ,  int  pos  ,  int  num  ,  string  R  ) 

{ 

if  (  x  ==  0  ) 

{ 

now  [  num  ]  =  '\0'  ; 

subset  .  push_back  (  now  )  ; 

return  ; 

} 

FOR  (  i  ,  pos  ,  R  .  length  (  )  ) 

{ 

now  [  num  ]  =  R  [  i  ]  ; 

get_subset  (  x  \-  1  ,  i  \+  1  ,  num  \+  1  ,  R  )  ; 

} 

} 

void  Attribute  ::  all_subset  (  string  R  ) 

{ 

FOR  (  i  ,  0  ,  R  .  length  (  )  ) 

get_subset  (  i  \+  1  ,  0  ,  0  ,  R  )  ; 

} 

//判断 a 是否为候选码 

bool  Attribute  ::  is_candidate_key  (  string  a  ) 

{ 

FOR  (  i  ,  0  ,  key  .  size  (  )  ) 

if  (  s_in_s  (  key  [  i  ]  ,  a  )  ) 

return  false  ; 

return  true  ; 

} 

// 求码 

void  Attribute  ::  candidate_key  (  vss  F  ,  string  R  ) 

{ 

vs  ans  ; 

subset  .  clear  (  )  ; 

all_subset  (  R  )  ; 

EKey  .  clear  (  )  ; 

key  .  clear  (  )  ; 

FOR  (  i  ,  0  ,  subset  .  size  (  )  ) 

if  (  closure_attribute  (  subset  [  i  ]  ,  F  )  .  length  (  )  ==  R  .  length  (  )  ) 

{ 

EKey  .  push_back  (  subset  [  i  ]  )  ; 

if  (  !  is_candidate_key  (  subset  [  i  ]  )  ) 

continue  ; 

key  .  push_back  (  subset  [  i  ]  )  ; 

} 

} 

// 求极小覆盖 

vss  Attribute  ::  minimum_cover  (  ) 

{ 

vss  MC  =  F  ; 

// 右部极小化 

FOR  (  i  ,  0  ,  MC  .  size  (  )  ) 

{ 

if  (  MC  [  i  ]  .  second  .  size  (  )  !=  1  ) 

{ 

string  s  =  MC  [  i  ]  .  first  ; 

string  y  =  MC  [  i  ]  .  second  ; 

string  t  =  ""  ; 

t  +=  y  [  0  ]  ; 

MC  [  i  ]  .  second  =  t  ; 

FOR  (  k  ,  1  ,  y  .  size  (  )  ) 

{ 

t  =  y  [  k  ]  ; 

MC  .  push_back  (  make_pair  (  s  ,  t  )  )  ; 

} 

} 

} 

// 左部极小化 

FOR  (  i  ,  0  ,  MC  .  size  (  )  ) 

{ 

if  (  MC  [  i  ]  .  first  .  size  (  )  !=  1  ) 

{ 

string  s  =  MC  [  i  ]  .  first  ; 

string  ans  =  ""  ; 

bool  del  [  MAX  ]  ; 

memset  (  del  ,  false  ,  sizeof  (  del  )  )  ; 

FOR  (  k  ,  0  ,  s  .  size  (  )  ) 

{ 

string  la  =  ""  ; 

FOR  (  j  ,  0  ,  s  .  size  (  )  ) 

if  (  !  del  [  j  ]  && k  !=  j  ) 

la  +=  s  [  j  ]  ; 

string  att  =  closure_attribute  (  la  ,  MC  )  ; 

if  (  s_in_s  (  MC  [  i  ]  .  second  ,  att  )  ) 

del  [  k  ]  =  true  ; 

} 

FOR  (  j  ,  0  ,  s  .  size  (  )  ) 

if  (  !  del  [  j  ]  ) 

ans  +=  s  [  j  ]  ; 

MC  [  i  ]  .  first  =  ans  ; 

} 

} 

sort  (  MC  .  begin  (  )  ,  MC  .  end  (  )  )  ; 

MC  .  resize  (  unique  (  MC  .  begin  (  )  ,  MC  .  end  (  )  )  \-  MC  .  begin  (  )  )  ; 

// 去掉传递依赖 

vss  MCC  ; 

FOR  (  i  ,  0  ,  MC  .  size  (  )  ) 

{ 

vss  tmp  =  MC  ; 

tmp  .  erase  (  tmp  .  begin  (  )  \+  i  )  ; 

tmp  .  resize  (  MC  .  size  (  )  \-  1  )  ; 

string  la  =  closure_attribute  (  MC  [  i  ]  .  first  ,  tmp  )  ; 

if  (  !  s_in_s  (  MC  [  i  ]  .  second  ,  la  )  ) 

MCC  .  push_back  (  MC  [  i  ]  )  ; 

} 

return  MCC  ; 

} 

vss  Attribute  ::  right_cover  (  ) 

{ 

vss  MC  =  minimum_cover  (  )  ; 

vss  MCC  ; 

bool  f  [  2000  ]  ; 

memset  (  f  ,  false  ,  sizeof  (  f  )  )  ; 

FOR  (  i  ,  0  ,  MC  .  size  (  )  ) 

{ 

if  (  f  [  i  ]  )  continue  ; 

string  la  =  MC  [  i  ]  .  second  ; 

FOR  (  k  ,  i  \+  1  ,  MC  .  size  (  )  ) 

if  (  !  f  [  k  ]  && MC  [  k  ]  .  first  ==  MC  [  i  ]  .  first  ) 

{ 

f  [  k  ]  =  true  ; 

la  +=  MC  [  k  ]  .  second  ; 

} 

MCC  .  push_back  (  make_pair  (  MC  [  i  ]  .  first  ,  l   
  
---|---
#### 原文：[http://www.xysay.com/database-cpp-115.html](http://www.xysay.com/database-cpp-115.html)