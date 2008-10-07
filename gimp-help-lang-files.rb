require 'getoptlong'

options = 
  ['--prefix', '-p', GetoptLong::REQUIRED_ARGUMENT],
  ['--skip', '-s', GetoptLong::REQUIRED_ARGUMENT]
  
opts = GetoptLong.new(*options)

prefix = []
skip = []

opts.each do |opt, arg|
  case opt
    when '--prefix'
      prefix.push arg
    when '--skip'
      skip.push arg
  end
end

prefix.each do |p|
  s = ''
  p.split(%r@#{File::SEPARATOR}@).each do |d|
    s = s + (( s == File::SEPARATOR ) ? d : File::SEPARATOR + d) # to avoid // in paths
    skip.push "^#{s}$"
  end
end

skip.map! { |x| "path !~ %r@#{x}@ "}
reskip = ''
skip.each {|x| reskip = reskip + ((reskip == '') ? x : ' && ' + x)}

dir = ARGV.shift

if dir == nil
  if ENV["RPM_BUILD_ROOT"] === nil
    raise "ERROR: Neither directory nor RPM_BUILD_ROOT env. var. is set."
  else
    dir = ENV["RPM_BUILD_ROOT"]
  end
end

dirs = []
files = []
odd = []

require 'find'
Find.find(dir) do |rpath|
  path = rpath.sub(%r@^#{dir}@, '')
  if FileTest.directory?(rpath) && path.length > 0 && rpath !~ %r@^\.{1,2}@ && eval(reskip)
    if path !~ %r@(/en/)|(/en$)@ && path =~ %r@(/([a-z]{2})/)|(/([a-z]{2})$)@
      dirs.push "%dir %lang(#{$2}#{$4}) #{path}"
    else
      dirs.push "%dir #{path}"
    end
  elsif FileTest.file?(rpath) && eval(reskip) 
    if path !~ %r@/en/@ && path =~ %r@/([a-z]{2})/@
      files.push "%lang(#{$1}) #{path}"
    else
      files.push path
    end
  else
    odd.push path
  end
end

dirs.each {|x| puts "#{x}" }
files.each {|x| puts "#{x}" }
#odd.each {|x| puts "odd: #{x}" }
